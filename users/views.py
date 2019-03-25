from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from booking.models import Booking, BookedTicket, Ticket

from .forms import CustomUserCreationForm

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


@user_passes_test(lambda u: u.is_superuser)
def AdminTools(request):
    return render(request, 'users/admin_tools.html')


@login_required
def listTickets(request):
    userOwnedBookings = Booking.objects.all().filter(paid_by=request.user).order_by('datetime')
    userOwnedTickets = []

    for booking in userOwnedBookings:
        for bookedTicket in BookedTicket.objects.all().filter(booking=booking):
            userOwnedTickets.append(bookedTicket)

    context = {'bookedTickets': userOwnedTickets}

    return render(request, 'users/ticket_list.html', context)
