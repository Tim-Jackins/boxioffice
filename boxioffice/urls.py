from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include 
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

from contact import views as cont_views
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='home'),
    url(r'^contact/$', cont_views.contact,name='contact'),
    
    url(r'^markdownx/', include('markdownx.urls')),

    path('booking/', include('booking.urls')),
    path('players/', include('players.urls')),
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

# For django_markdown
urlpatterns += [
    url(r'^markdownx/', include('markdownx.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #all values set in settings.py
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
