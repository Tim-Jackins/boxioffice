
from django.urls import path
from . import views

'''
urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('admintools/', views.AdminTools, name='adminTools'),
    path('tickets/', views.listTickets, name='ticket_list'),
]
'''

urlpatterns = [
    path('', views.show_index,name='booking'),
    path('<int:pk>/', views.ShowDetails.as_view(), name='show_details'),    
    path('payment/', views.payment_gateway, name='payment_gateway'),
    path('confirmation/', views.payment_confirmation, name='payment_confirmation'),
]

'''
url(r'^booking/seatchoice/(?P<pk>\d+)/$', booking_views.reserve_seat, name='reserve_seat'),



url(r'^booking/theater/seats/(?P<pk>\d+)/$', booking_views.TheaterSeatsJSON, name='theater_seats'),
#Hard Coded templates i.e. without views.
url(r'^booking/payment/booking/seatnotfound.html$', TemplateView.as_view(template_name="booking/seatnotfound.html"), name='seatnotfound'),
url(r'^booking/payment_confirmation/booking/seatconflict.html$', TemplateView.as_view(template_name="booking/seatconflict.html"), name='seatconflict'),
url(r'^booking/payment_confirmation/booking/payment_cancelled.html$', TemplateView.as_view(template_name="booking/payment_cancelled.html"), name='payment_cancelled'),
'''