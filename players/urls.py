from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.ActorDetailView.as_view(), name='actor_detail'),
]
