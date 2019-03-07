from django.contrib import admin

# Register your models here.
from .models import Show, Theater, Showing, Booking, Ticket, BookedTicket


class ShowAdmin(admin.ModelAdmin):
	class Meta:
		model = Show

admin.site.register(Show,ShowAdmin)


class TheaterAdmin(admin.ModelAdmin):
	class Meta:
		model = Theater

admin.site.register(Theater,TheaterAdmin)


class ShowingAdmin(admin.ModelAdmin):
	class Meta:
		model = Showing

admin.site.register(Showing,ShowingAdmin)


class BookingAdmin(admin.ModelAdmin):
	class Meta:
		model = Booking

admin.site.register(Booking,BookingAdmin)


class TicketAdmin(admin.ModelAdmin):
	class Meta:
		model = Ticket

admin.site.register(Ticket,TicketAdmin)


class BookedTicketAdmin(admin.ModelAdmin):
	class Meta:
		model = BookedTicket

admin.site.register(BookedTicket,BookedTicketAdmin)
