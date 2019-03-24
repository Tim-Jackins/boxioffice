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


class BookingAdmin(admin.ModelAdmin):
	class Meta:
		model = Booking

admin.site.register(Booking,BookingAdmin)


class TicketAdmin(admin.ModelAdmin):
	class Meta:
		model = Ticket

admin.site.register(Ticket,TicketAdmin)


def makeTickets(modeladmin, request, queryset):
	for showing in queryset:
		showing.generateTickets()
makeTickets.short_description = 'Generate Tickets'


class ShowingAdmin(admin.ModelAdmin):
	class Meta:
		model = Showing

	actions = [makeTickets, ]

admin.site.register(Showing,ShowingAdmin)


class BookedTicketAdmin(admin.ModelAdmin):
	class Meta:
		model = BookedTicket

admin.site.register(BookedTicket,BookedTicketAdmin)
