from django.db import models
from django.conf import settings
from allauth.account.signals import user_logged_in, user_signed_up
#from django.core.validators import validate_comma_separated_integer_list
import datetime
from booking.models import Show
from hashlib import md5
from time import time
import uuid

class Actor(models.Model):
    firstname           = models.CharField(max_length=15)
    lastname            = models.CharField(max_length=15)
    email               = models.EmailField()
    dob                 = models.DateField()
    bio                 = models.TextField(max_length=280)
    headshot            = models.ImageField(help_text='Make sure your headshot is 8in x 10in.', upload_to='headshots')
    
    def __str__(self):
        return f'{self.firstname} {self.lastname} ({self.dob})'

class Role(models.Model):
    is_ensemble         = models.BooleanField(default=True)
    part_name           = models.CharField(max_length=15, null=False, default='')
    main_actor          = models.ForeignKey(
        'Actor', 
        related_name="main_actor",
        related_query_name="main_actor",
        on_delete=models.CASCADE
    )
    understudy1         = models.ForeignKey(
        'Actor', 
        related_name="understudy1_actor",
        related_query_name="understudy1_actor",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    understudy2         = models.ForeignKey(
        'Actor', 
        related_name="understudy2_actor",
        related_query_name="understudy2_actor",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    show            = models.ForeignKey(Show, on_delete=models.CASCADE)
    

    def __str__(self):
        return f'{self.part_name} by {self.main_actor} for {self.show}'
