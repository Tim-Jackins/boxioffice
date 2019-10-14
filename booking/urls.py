from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_index,name='booking'),
    path('<int:pk>/', views.ShowDetails.as_view(), name='show_details'),    
    path('payment/', views.payment_gateway, name='payment_gateway'),
    path('confirmation/', views.payment_confirmation, name='payment_confirmation'),
    path('theater/seats/<int:pk>/', views.TheaterSeatsJSON, name='theater_seats')
]
