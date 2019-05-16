#pylint: disable-msg=no-member
# the login_required decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *
from django.core.mail import send_mail
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.urls import reverse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404, JsonResponse

from paypal.standard.forms import PayPalPaymentsForm

from boxioffice.settings import EMAIL_HOST
from .forms import BookingForm, SelectedTicketForm
import datetime
import uuid
import json


def getAvailableTickets(allTickets):
    availableTickets = []
    for ticket in allTickets:
        if not BookedTicket.objects.filter(ticket=ticket).exists():
            availableTickets.append(ticket)
    return availableTickets


@login_required
def reserve_seat(request, pk):
    try:
        show_info = Showing.objects.get(pk=pk)
    except Show.DoesNotExist:
        raise handler404("Page Does Not Exist.")
    form = SelectedTicketForm()
    context = {'show_info': show_info, 'form': form}

    return render(request, 'booking/reserve_seat.html', context)


@login_required
def payment_gateway(request):
    if request.POST:
        number_of_tickets = int(request.POST.get('number_of_tickets'))
        showing_id = request.POST.get('showing_id')
        showing = Showing.objects.get(pk=showing_id)
        availableTickets = getAvailableTickets(Ticket.objects.all())

        if number_of_tickets > len(availableTickets):
            context = {
                'show_id': showing.show.id,
                'tickets_left': len(availableTickets),
            }
            return render(request, 'booking/not_enough_tickets.html', context)

        '''
            print(f'Seats={number_of_tickets} show: {showing}')

            if number_of_tickets < 

            allTickets = Ticket.objects.filter(showing=showing)
            
            openTickets = []

            for ticket in allTickets:
                try:
                    BookedTicket.objects.get(ticket=ticket)
                except:
                    openTickets.append(ticket)

            if len(openTickets) < number_of_tickets:
                return redirect(reverse('seatnotfound'))
            
            form = BookingForm()
        '''

        total_price = showing.cost * number_of_tickets
        invoice_uuid = uuid.uuid4

        # What you want the button to do.
        paypal_dict = {
            "business": EMAIL_HOST,
            "amount": total_price,
            "item_name": f'{number_of_tickets} tickets for {showing}',
            "invoice": invoice_uuid,
            'currency_code': 'USD',
            "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
            "return": request.build_absolute_uri(reverse('payment_gateway')),
            "cancel_return": request.build_absolute_uri(reverse('payment_cancelled')),
        }

        form = PayPalPaymentsForm(initial=paypal_dict)

        context = {
            'number_of_tickets': number_of_tickets,
            'showing': showing,
            'form': form,
            'total_price': total_price,
            'invoice': invoice_uuid,
        }

        return render(request, 'booking/payment_gateway.html', context)

    else:
        return redirect('/booking/')


@csrf_exempt
def payment_confirmation(request):
    showing_id = request.POST.get('showing_id')
    showing = Showing.objects.get(pk=showing_id)
    number_of_tickets = eval(request.POST.get('number_of_tickets'))

    paid_amount = eval(request.POST.get('amount').replace('$', ''))
    paid_by = request.user
    invoice = request.POST.get('invoice')

    # For now generate booking on payment confirmation
    booking = Booking(
        paid_amount=paid_amount,
        paid_by=paid_by,
        invoice=invoice,
    )

    booking.save()
    print(booking.id)

    tickets = getAvailableTickets(Ticket.objects.all())[:number_of_tickets]

    print(f'Booking these tickets: {tickets}')

    for ticket in tickets:
        tempBookedTicket = BookedTicket(
            ticket=ticket,
            booking=booking,
        )
        tempBookedTicket.save()

    return render(request, 'booking/payment_confirmation.html')


@csrf_exempt
def payment_cancelled(request):
    return render(request, 'booking/payment_cancelled.html')


def show_list(request):
    shows = Show.objects.all().order_by('name')
    print(f'\n\nshows\n\n')
    show_list = []
    show_by_lang = []
    lang = shows[0].language
    for i in range(0, len(shows)):
        if lang != shows[i].language:
            lang = shows[i].language
            show_list.append(show_by_lang)
            show_by_lang = []
        show_by_lang.append(shows[i])

    show_list.append(show_by_lang)

    return render(request, 'booking/show_list.html', {'shows': show_list})


class ShowDetails(View):
    template = 'booking/show_details.html'
    def get(self, request, pk, *args, **kwargs):
        try:
            show_info = Show.objects.get(pk=pk)
            showing_list = Showing.objects.filter(show=pk).order_by('datetime')
            dateDict = {'dates': []}
            for showing in showing_list:
                dateDict['dates'].append(showing.datetime.strftime('%c'))
            theater = show_info.theater
        except Show.DoesNotExist:
            raise Http404("Show does not exist")

        props = {
            'seatDataJSON': json.dumps(theater.seating_chart),
            'dateDataJSON': json.dumps(dateDict),
        }

        context = {
            'props': props,
            'show_info': show_info,
            'showing_list': showing_list
        }

        return render(request, self.template, context)


def ShowDetailsJSON(request, pk):
    def get(self, request, pk, *args, **kwargs):
        try:
            show_info = Show.objects.get(pk=pk)
            showing_list = Showing.objects.filter(show=pk).order_by('datetime')
            dateDict = {'dates': []}
            for showing in showing_list:
                dateDict['dates'].append(showing.datetime.strftime('%c'))
            theater = show_info.theater
        except Show.DoesNotExist:
            raise Http404("Show does not exist")

        props = {
            'seatDataJSON': json.dumps(theater.seating_chart),
            'dateDataJSON': json.dumps(dateDict),
        }

        return JsonResponse(props)


def theater_list(request):
    theaters = Theater.objects.all().order_by('city')
    theater_list = []
    theater_by_city = []
    city = theaters[0].city
    for i in range(0, len(theaters)):
        if city != theaters[i].city:
            city = theaters[i].city
            theater_list.append(theater_by_city)
            theater_by_city = []
        theater_by_city.append(theaters[i])

    theater_list.append(theater_by_city)

    return render(request, 'theater/theater_list.html', {'theaters': theater_list})


def theater_details(request, theater_id):
    try:
        theater_info = Theater.objects.get(pk=theater_id)
        shows = Show.objects.filter(theater=theater_id,
                                    date=datetime.date.today()).order_by('show')

        show_list = []
        show_by_show = []
        show = shows[0].show
        for i in range(0, len(shows)):
            if show != shows[i].show:
                show = shows[i].show
                show_list.append(show_by_show)
                show_by_show = []
            show_by_show.append(shows[i])

        show_list.append(show_by_show)

        print(show_list)

    except Theater.DoesNotExist:
        raise Http404('Theater does not exist')
    return render(request, 'theater/theater_details.html',
                  {'theater_info': theater_info, 'show_list': show_list})


def TheaterSeatsJSON(request, pk):
    try:
        theater = Theater.objects.get(pk=pk)
        theaterChart = theater.seating_chart
    except Theater.DoesNotExist:
        raise Http404('Theater does not exist')
    return JsonResponse(theaterChart)


def show_index(request):
    show_list = Show.objects.all()
    date_details = []

    for show in show_list:
        tempShowing = show.showing_set.order_by('datetime')
        date_details += [{
            'start_date': show.showing_set.order_by('datetime').first().datetime.strftime('%b. %d'),
            'end_date': show.showing_set.order_by('datetime').last().datetime.strftime('%b. %d'),
        }]

    return render(request, 'common/booking.html', {'all_details_list': zip(show_list, date_details)})
