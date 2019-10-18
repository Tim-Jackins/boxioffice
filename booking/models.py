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
import jsonfield
import pprint
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

pp = pprint.PrettyPrinter(indent=4)

defaultSeatChart = '''{
    "seatLayout": {
        "colAreas": {
            "Count": 2,
            "intMaxSeatId": 11,
            "intMinSeatId": 1,
            "objArea": [
                {
                    "AreaDesc": "Standard",
                    "AreaId": "1",
                    "HasCurrentOrder": true,
                    "objRow": [
                        {
                            "GridRowId": 1,
                            "PhyRowId": "A",
                            "objSeat": [
                              {
                                  "GridSeatNum": 1,
                                  "SeatStatus": "0",
                                  "SeatNumber": 1
                              },
                                {
                                  "GridSeatNum": 2,
                                  "SeatStatus": "1",
                                  "SeatNumber": 2
                              },
                                {
                                  "GridSeatNum": 3,
                                  "SeatStatus": "1",
                                  "SeatNumber": 3
                              },
                                {
                                  "GridSeatNum": 4,
                                  "SeatStatus": "1",
                                  "SeatNumber": 4
                              },
                                {
                                  "GridSeatNum": 5,
                                  "SeatStatus": "0",
                                  "SeatNumber": 5
                              },
                                {
                                  "GridSeatNum": 6,
                                  "SeatStatus": "0",
                                  "SeatNumber": 6
                              },
                                {
                                  "GridSeatNum": 7,
                                  "SeatStatus": "0",
                                  "SeatNumber": 7
                              },
                                {
                                  "GridSeatNum": 8,
                                  "SeatStatus": "0",
                                  "SeatNumber": 8
                              },
                                {
                                  "GridSeatNum": 9,
                                  "SeatStatus": "0",
                                  "SeatNumber": 9
                              },
                                {
                                  "GridSeatNum": 10,
                                  "SeatStatus": "0",
                                  "SeatNumber": 10
                              }
                            ]
                        },
                        {
                            "GridRowId": 2,
                            "PhyRowId": "B",
                            "objSeat": [
                                {
                                    "GridSeatNum": 1,
                                    "SeatStatus": "0",
                                    "SeatNumber": 1
                                },
                                {
                                    "GridSeatNum": 2,
                                    "SeatStatus": "0",
                                    "SeatNumber": 2
                                },
                                {
                                    "GridSeatNum": 3,
                                    "SeatStatus": "0",
                                    "SeatNumber": 3
                                },
                                {
                                    "GridSeatNum": 4,
                                    "SeatStatus": "0",
                                    "SeatNumber": 4
                                },
                                {
                                    "GridSeatNum": 5,
                                    "SeatStatus": "0",
                                    "SeatNumber": 5
                                },
                                {
                                    "GridSeatNum": 6,
                                    "SeatStatus": "0",
                                    "SeatNumber": 6
                                },
                                {
                                    "GridSeatNum": 7,
                                    "SeatStatus": "0",
                                    "SeatNumber": 7
                                },
                                {
                                    "GridSeatNum": 8,
                                    "SeatStatus": "0",
                                    "SeatNumber": 8
                                },
                                {
                                    "GridSeatNum": 9,
                                    "SeatStatus": "0",
                                    "SeatNumber": 9
                                },
                                {
                                    "GridSeatNum": 10,
                                    "SeatStatus": "0",
                                    "SeatNumber": 10
                                }
                            ]
                        },
                        {
                            "GridRowId": 3,
                            "PhyRowId": "C",
                            "objSeat": [
                                {
                                    "GridSeatNum": 1,
                                    "SeatStatus": "0",
                                    "SeatNumber": 1
                                },
                                {
                                    "GridSeatNum": 2,
                                    "SeatStatus": "0",
                                    "SeatNumber": 2
                                },
                                {
                                    "GridSeatNum": 3,
                                    "SeatStatus": "0",
                                    "SeatNumber": 3
                                },
                                {
                                    "GridSeatNum": 4,
                                    "SeatStatus": "0",
                                    "SeatNumber": 4
                                },
                                {
                                    "GridSeatNum": 5,
                                    "SeatStatus": "0",
                                    "SeatNumber": 5
                                },
                                {
                                    "GridSeatNum": 6,
                                    "SeatStatus": "0",
                                    "SeatNumber": 6
                                },
                                {
                                    "GridSeatNum": 7,
                                    "SeatStatus": "0",
                                    "SeatNumber": 7
                                },
                                {
                                    "GridSeatNum": 8,
                                    "SeatStatus": "0",
                                    "SeatNumber": 8
                                },
                                {
                                    "GridSeatNum": 9,
                                    "SeatStatus": "0",
                                    "SeatNumber": 9
                                },
                                {
                                    "GridSeatNum": 10,
                                    "SeatStatus": "0",
                                    "SeatNumber": 10
                                }
                            ]
                        }
                    ]
                },
                {
                    "AreaDesc": "Side seating",
                    "AreaId": "1",
                    "HasCurrentOrder": true,
                    "objRow": [
                        {
                            "GridRowId": 3,
                            "PhyRowId": "D",
                            "objSeat": [
                              {
                                  "GridSeatNum": 1,
                                  "SeatStatus": "0",
                                  "SeatNumber": 1
                              },
                                {
                                  "GridSeatNum": 2,
                                  "SeatStatus": "0",
                                  "SeatNumber": 2
                              },
                                {
                                  "GridSeatNum": 3,
                                  "SeatStatus": "0",
                                  "SeatNumber": 3
                              },
                                {
                                  "GridSeatNum": 8,
                                  "SeatStatus": "0",
                                  "SeatNumber": 4
                              },
                                {
                                  "GridSeatNum": 9,
                                  "SeatStatus": "0",
                                  "SeatNumber": 5
                              },
                                {
                                  "GridSeatNum": 10,
                                  "SeatStatus": "0",
                                  "SeatNumber": 6
                              }
                            ]
                        },
                        {
                            "GridRowId": 3,
                            "PhyRowId": "E",
                            "objSeat": [
                                {
                                    "GridSeatNum": 1,
                                    "SeatStatus": "0",
                                    "SeatNumber": 1
                                },
                                {
                                    "GridSeatNum": 2,
                                    "SeatStatus": "0",
                                    "SeatNumber": 2
                                },
                                {
                                    "GridSeatNum": 3,
                                    "SeatStatus": "0",
                                    "SeatNumber": 3
                                },
                                {
                                    "GridSeatNum": 8,
                                    "SeatStatus": "0",
                                    "SeatNumber": 4
                                },
                                {
                                    "GridSeatNum": 9,
                                    "SeatStatus": "0",
                                    "SeatNumber": 5
                                },
                                {
                                    "GridSeatNum": 10,
                                    "SeatStatus": "0",
                                    "SeatNumber": 6
                                }
                            ]
                        },
                        {
                            "GridRowId": 3,
                            "PhyRowId": "F",
                            "objSeat": [
                                {
                                    "GridSeatNum": 1,
                                    "SeatStatus": "0",
                                    "SeatNumber": 1
                                },
                                {
                                    "GridSeatNum": 2,
                                    "SeatStatus": "0",
                                    "SeatNumber": 2
                                },
                                {
                                    "GridSeatNum": 3,
                                    "SeatStatus": "0",
                                    "SeatNumber": 3
                                },
                                {
                                    "GridSeatNum": 8,
                                    "SeatStatus": "0",
                                    "SeatNumber": 4
                                },
                                {
                                    "GridSeatNum": 9,
                                    "SeatStatus": "0",
                                    "SeatNumber": 5
                                },
                                {
                                    "GridSeatNum": 10,
                                    "SeatStatus": "0",
                                    "SeatNumber": 6
                                }
                            ]
                        }
                    ]
                },
                {
                    "AreaDesc": "VIP Tables",
                    "AreaId": "2",
                    "HasCurrentOrder": true,
                    "objRow": [
                        {
                            "GridRowId": 4,
                            "PhyRowId": "T",
                            "objSeat": [
                              {
                                  "GridSeatNum": 1,
                                  "SeatStatus": "0",
                                  "SeatNumber": 1
                              },
                                {
                                  "GridSeatNum": 2,
                                  "SeatStatus": "0",
                                  "SeatNumber": 2
                              },
                                {
                                  "GridSeatNum": 5,
                                  "SeatStatus": "0",
                                  "SeatNumber": 3
                              },
                                {
                                  "GridSeatNum": 6,
                                  "SeatStatus": "0",
                                  "SeatNumber": 4
                              },
                                {
                                  "GridSeatNum": 9,
                                  "SeatStatus": "0",
                                  "SeatNumber": 5
                              },
                                {
                                  "GridSeatNum": 10,
                                  "SeatStatus": "0",
                                  "SeatNumber": 6
                              }
                            ]
                        },
                        {
                            "GridRowId": 4,
                            "PhyRowId": "TT",
                            "objSeat": [
                                {
                                    "GridSeatNum": 1,
                                    "SeatStatus": "0",
                                    "SeatNumber": 1
                                },
                                {
                                    "GridSeatNum": 2,
                                    "SeatStatus": "0",
                                    "SeatNumber": 2
                                },
                                {
                                    "GridSeatNum": 5,
                                    "SeatStatus": "0",
                                    "SeatNumber": 3
                                },
                                {
                                    "GridSeatNum": 6,
                                    "SeatStatus": "0",
                                    "SeatNumber": 4
                                },
                                {
                                    "GridSeatNum": 9,
                                    "SeatStatus": "0",
                                    "SeatNumber": 5
                                },
                                {
                                    "GridSeatNum": 10,
                                    "SeatStatus": "0",
                                    "SeatNumber": 6
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    },
    "areas": [],
    "groupedSeats": []
}'''


class Show(models.Model):
    lang_choice = (
        ('ENGLISH', 'English'),
    )

    name = models.CharField(max_length=20)
    director = models.CharField(max_length=20, blank=True)
    theater = models.ForeignKey(
        'Theater', on_delete=models.CASCADE, null=True, blank=True)
    language = models.CharField(max_length=10, choices=lang_choice)
    description = MarkdownxField(default='This is an empty description.')
    run_length = models.IntegerField(
        help_text="Enter run length in minute's", null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='media', max_length=255)

    @property
    def length(self):
        return f'{self.run_length} minutes'

    def __str__(self):
        return self.name


class Theater(models.Model):
    name = models.CharField(max_length=50)
    location_link = models.CharField(
        help_text='Copy the goo.gl share link from google maps', max_length=32, null=True, blank=True)
    frame_link = models.CharField(
        help_text='Click "Copy Link" then Embed a map the src lin in this field', max_length=400, null=True, blank=True)
    seating_chart = jsonfield.JSONField(
        default='',
        help_text='Enter the JSON seating chart')
    max_occupancy = models.IntegerField(
        default=60,
        help_text='Enter the total number of seats.')

    def __str__(self):
        return self.name


class Showing(models.Model):
    datetime = models.DateTimeField()
    show = models.ForeignKey('Show', on_delete=models.CASCADE)
    cost = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')

    def generateTickets(self):
        try:
            Ticket.objects.get(showing=self)
        except ObjectDoesNotExist:
            showingTickets = []

            seatChart = self.show.theater.seating_chart['seatLayout']['colAreas']['objArea']

            for section in seatChart:
                for row in section['objRow']:
                    for seat in row['objSeat']:
                        showingTickets.append(
                            Ticket(
                                showing=self,
                                AreaDesc=section['AreaDesc'],
                                PhyRowId=row['PhyRowId'],
                                SeatNumber=seat['SeatNumber'],
                                seatId=row['PhyRowId']+str(seat['SeatNumber'])
                            )
                        )

            print(
                f'Generating tickets for showing {self.show} at {self.datetime}')

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
        ('STRIPE'),
        ('CASH')
    )

    receipt = models.CharField(max_length=120, null=True, blank=True)
    payment_method = models.CharField(max_length=7, null=True, blank=True)
    stripe_id = models.CharField(max_length=27, null=True, blank=True)

    datetime = models.DateTimeField(default=now, editable=False)
    paid_amount = MoneyField(
        decimal_places=2, max_digits=10, default_currency='USD', null=True, blank=True)
    paid_by = models.ForeignKey(
        get_user_model(), on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return f'{self.datetime} | {self.paid_by}'


class Ticket(models.Model):
    AreaDesc = models.CharField(default='standard', max_length=50)
    PhyRowId = models.CharField(default='X', max_length=50)
    SeatNumber = models.IntegerField(default=1, max_length=50)
    seatId = models.CharField(default='X1', max_length=50)

    available = models.BooleanField(default=True)

    showing = models.ForeignKey(Showing, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.seatId}-{self.showing}' + ('' if self.available else '-SOLD')

class BookedTicket(models.Model):
    ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)

    def safe_delete(self, *args, **kwargs):
        connected_ticket = self.ticket#Ticket.objects.get(pk=self.ticket.primary_key)
        connected_ticket.available = True
        connected_ticket.save()
        super(BookedTicket, self).delete(*args, **kwargs)

    def __str__(self):
        return str(self.ticket) + ' | ' + str(self.booking)
