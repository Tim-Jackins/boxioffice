from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from allauth.account.signals import user_logged_in, user_signed_up
from django.utils.timezone import now
#from django.core.validators import validate_comma_separated_integer_list
import datetime
import uuid
from django.db import models
from djmoney.models.fields import MoneyField
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

class Show(models.Model):
    lang_choice = (
        ('ENGLISH', 'English'),
    )

    name                = models.CharField(max_length=20)
    director            = models.CharField(max_length=20, blank=True)
    language            = models.CharField(max_length=10, choices=lang_choice)
    run_length          = models.IntegerField(help_text="Enter run length in minute's", null=True, blank=True)
    image               = models.ImageField(null=True, blank=True, upload_to='media')

    @property
    def length(self):
        return f'{self.run_length} minutes'

    def __str__(self):
        return self.name


class Theater(models.Model):
    name                = models.CharField(max_length=50)
    max_occupancy       = models.IntegerField(default=20)
    location_link       = models.CharField(help_text='Copy the goo.gl share link from google maps', max_length=32, null=True, blank=True)
    frame_link          = models.CharField(help_text='Click "Copy Link" then Embed a map the src lin in this field', max_length=400, null=True, blank=True)

    def __str__(self):
        return self.name


class Showing(models.Model):
    datetime            = models.DateTimeField()
    show                = models.ForeignKey('Show', on_delete=models.CASCADE)
    theater             = models.ForeignKey('Theater', on_delete=models.CASCADE,null=True,blank=True)
    cost                = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')

    def generateTickets(self):
        try:
            Ticket.objects.get(showing=self)
        except ObjectDoesNotExist:
            showingTickets = []
            print(f'Generating tickets for showing {self.show} at {self.datetime}')
            for each in range(self.theater.max_occupancy):
                showingTickets.append(Ticket(showing=self))
            Ticket.objects.bulk_create(showingTickets)
        except:
            print('Ticket\'s have already been generated')


    def __str__(self):
        try:
            Ticket.objects.get(showing=self)
        except ObjectDoesNotExist:
            return 'SHOW HAS NO TICKETS'
        except:
            return f'{self.show} at {self.datetime}'


class Booking(models.Model):
    payment_choice = (
        ('PAYPAL', 'PayPal'),
    )

    invoice             = models.UUIDField(null=True,blank=True)
    datetime            = models.DateTimeField(default=now, editable=False)
    payment_type        = models.CharField(max_length=11, choices=payment_choice, default='PayPal')
    paid_amount         = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', null=True, blank=True)
    paid_by             = models.ForeignKey(get_user_model(),on_delete=models.DO_NOTHING,null=True,blank=True)

    def __str__(self):
        return f'{self.datetime} | {self.paid_by}'


class Ticket(models.Model):
    showing             = models.ForeignKey(Showing, on_delete=models.CASCADE)
    uuid                = models.UUIDField(default=uuid.uuid4, editable=False)
    
    def __str__(self):
        return f'{self.uuid}'

class BookedTicket(models.Model):
    ticket              = models.OneToOneField(Ticket, on_delete=models.CASCADE)
    booking             = models.ForeignKey(Booking, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.ticket) + ' | ' + str(self.booking)
