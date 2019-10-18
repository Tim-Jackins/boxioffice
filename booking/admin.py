from django.contrib import admin

# Register your models here.
from .models import Show, Theater, Showing, Booking, Ticket, BookedTicket


def makeTickets(modeladmin, request, queryset):
	for showing in queryset:
		showing.generateTickets()
makeTickets.short_description = 'Generate Tickets'


def makeTicketsAvailable(modeladmin, request, queryset):
	for ticket in queryset:
		ticket.available = True
		ticket.save()
makeTicketsAvailable.short_description = 'Make Tickets Available'


def safeDeleteBookedTicket(modeladmin, request, queryset):
	for bookedTicket in queryset:
		bookedTicket.safe_delete()
safeDeleteBookedTicket.short_description = 'Safe Delete Booked Ticket'


def safeDeleteBooking(modeladmin, request, queryset):
	for booking in queryset:
		for tempBookedTicket in BookedTicket.objects.filter(booking=booking):
			tempBookedTicket.safe_delete()
		booking.delete()
safeDeleteBooking.short_description = 'Safe Delete Booking'


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
	
	actions = [safeDeleteBooking, ]

admin.site.register(Booking,BookingAdmin)


class TicketAdmin(admin.ModelAdmin):
	class Meta:
		model = Ticket

	actions = [makeTicketsAvailable, ]

admin.site.register(Ticket,TicketAdmin)


class ShowingAdmin(admin.ModelAdmin):
	class Meta:
		model = Showing

	actions = [makeTickets, ]

admin.site.register(Showing,ShowingAdmin)



class BookedTicketAdmin(admin.ModelAdmin):
	class Meta:
		model = BookedTicket

	actions = [safeDeleteBookedTicket, ]

admin.site.register(BookedTicket,BookedTicketAdmin)
