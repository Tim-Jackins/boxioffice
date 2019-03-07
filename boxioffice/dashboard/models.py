from django.conf import settings
from django.db import models
#from allauth.account.signals import user_logged_in, user_signed_up
#import stripe

# Create your models here.
class dashboard(models.Model):
	username 			= models.CharField(max_length = 100)
	user 				= models.OneToOneField(settings.AUTH_USER_MODEL,null=True,blank=True, on_delete=models.CASCADE) #Note.imp.
	about 				= models.TextField(default = 'default about text')
	location 			= models.CharField(default="location default text",max_length = 200,blank=True)
	worktitle 			= models.CharField(max_length=100,null=True,blank=True)

	def __str__(self):  #used to display username on admin pages.
		return self.username
