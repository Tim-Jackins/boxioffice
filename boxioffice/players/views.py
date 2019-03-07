#pylint: disable-msg=no-member
from django.contrib.auth.decorators import login_required #the login_required decorator
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Actor, Role
from django.core.mail import send_mail
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views import generic


class ActorDetailView(generic.DetailView):
	model = Actor

'''
def handler404(request, *args, **argv):
    response = render_to_response('404.html', context=RequestContext(request))
    response.status_code = 404
    return response

def handler500(request, *args, **argv):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
'''
