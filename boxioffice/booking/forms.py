from django import forms
from .models import Ticket, Booking

class SelectedTicketForm(forms.Form):
    number_of_tickets = forms.CharField(required=True, max_length=10, help_text='How many tickets do you want to buy?')

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('payment_type',)
