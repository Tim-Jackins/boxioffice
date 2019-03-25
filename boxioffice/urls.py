from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static #for static files on local server.
from django.conf.urls import include 
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

from contact import views as cont_views
from booking import views as booking_views
from players import views as player_views
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='home'),
    url(r'^contact/$', cont_views.contact,name='contact'),
    url(r'^players/(?P<pk>\d+)/$', player_views.ActorDetailView.as_view(), name='actor-detail'),
    url(r'^booking/$', booking_views.show_index,name='booking'),
    url(r'^booking/(?P<pk>\d+)/$', booking_views.show_details, name='show_details'),
    url(r'^booking/seatchoice/(?P<pk>\d+)/$', booking_views.reserve_seat, name='reserve_seat'),
    url(r'^booking/payment/$', booking_views.payment_gateway, name='payment_gateway'),
    url(r'^booking/payment_confirmation/$', booking_views.payment_confirmation, name='payment_confirmation'),
    #Hard Coded templates i.e. without views.
    url(r'^booking/payment/booking/seatnotfound.html$', TemplateView.as_view(template_name="booking/seatnotfound.html"), name='seatnotfound'),
    url(r'^booking/payment_confirmation/booking/seatconflict.html$', TemplateView.as_view(template_name="booking/seatconflict.html"), name='seatconflict'),
    url(r'^booking/payment_confirmation/booking/payment_cancelled.html$', TemplateView.as_view(template_name="booking/payment_cancelled.html"), name='payment_cancelled'),

    url(r'^blog/', include('blog.urls')),
    url(r'^markdownx/', include('markdownx.urls')),
    
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),

    url(r'^favicon.ico$',
        RedirectView.as_view( # the redirecting function
            url=staticfiles_storage.url('img/favicon.ico'),
        ),
        name="favicon"
    ),
]

# For social django
urlpatterns += [
    #url(r'^$', core_views.home, name='home'),
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
]

# For PayPal IPN
urlpatterns += [
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
]

# For django_markdown
urlpatterns += [
    url(r'^markdownx/', include('markdownx.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #all values set in settings.py
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
