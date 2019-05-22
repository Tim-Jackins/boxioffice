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

from boxioffice.settings import EMAIL_HOST, STRIPE_PUBLISHABLE_KEY
from .forms import BookingForm, SelectedTicketForm
import datetime
import uuid
import json
from django.core.serializers.json import DjangoJSONEncoder


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


@csrf_exempt
def payment_cancelled(request):
    return render(request, 'booking/payment_cancelled.html')


@login_required
def payment_gateway(request):
    if request.POST:
        showId = json.loads(request.POST.get('showId'))
        show = Show.objects.get(pk=showId)

        seatsToBuy = json.loads(request.POST.get('Seats'))
        date = request.POST.get('Date')
        total_cost = request.POST.get('total_cost')

        q1 = Showing.objects.filter(show=show)
        print()
        print('DATA')
        
        #print(q1[0].datetime)

        #'2019-05-20 16:14:18+00:00'
        
        showing = q1.get(datetime=datetime.datetime.strptime(date, '%c').strftime('%Y-%m-%d %H:%M:%S+00:00'))

        props = {
            'cartInfo': json.dumps(seatsToBuy, cls=DjangoJSONEncoder)
        }

        context = {
            'props': props,
            'showId': json.dumps(showId, cls=DjangoJSONEncoder),
            'date': json.dumps(date, cls=DjangoJSONEncoder),
            'showing_id': showing.id,
            'stripePubKey': STRIPE_PUBLISHABLE_KEY,
            'total_cost': total_cost
        }
        print(context)
        print()

        return render(request, 'booking/checkout.html', context)

        ''' 
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

        ''''''
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
            
            form = BookingForm()'''
        '''

        total_price = showing.cost * number_of_tickets
        invoice_uuid = uuid.uuid4

        
        context = {
            'number_of_tickets': number_of_tickets,
            'showing': showing,
            'form': form,
            'total_price': total_price,
            'invoice': invoice_uuid,
        }

        return render(request, 'booking/payment_gateway.html', context)
        '''

    else:
        return redirect('/booking/')


@login_required
def payment_confirmation(request):

    '''
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
    '''


class ShowDetails(View):
    template = 'booking/show_details.html'
    def get(self, request, pk, *args, **kwargs):
        try:

            show = Show.objects.get(pk=pk)
            seatChart = show.theater.seating_chart['seatLayout']['colAreas']['objArea']
            

            showing_list = Showing.objects.filter(show=pk).order_by('datetime')
            
            dateDict = {}
            
            dictLength = 0
            for showing in showing_list:
                tempSoldTickets = []
                for ticket in Ticket.objects.filter(showing=showing).filter(available=False):
                    tempSoldTickets.append({
                        'AreaDesc': ticket.AreaDesc,
                        'PhyRowId': ticket.PhyRowId,
                        'SeatNumber': ticket.SeatNumber
                    })

                dateDict.update({
                    str(dictLength): {
                        'date': showing.datetime.strftime('%c'),
                        'soldSeats': [ tempSoldTickets ]
                    }
                })
                
                dictLength += 1
            dateDict.update({ 'length': dictLength })
            
            print(dateDict)

            theater = show.theater
        except Show.DoesNotExist:
            raise Http404("Show does not exist")

        props = {
            'seatDataJSON': json.dumps(theater.seating_chart, cls=DjangoJSONEncoder),
            'dateDataJSON': json.dumps(dateDict, cls=DjangoJSONEncoder),
            'showId': pk
        }

        context = {
            'props': props,
            'show_info': show,
            'showing_list': showing_list
        }

        return render(request, self.template, context)


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
