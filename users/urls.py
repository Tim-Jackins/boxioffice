from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('admintools/', views.AdminTools, name='adminTools'),
    path('tickets/', views.listTickets, name='ticket_list'),
]
