from django.forms import modelform_factory
from django.shortcuts import render, render_to_response, redirect,get_object_or_404
from django.views import generic

from django.http import HttpResponseRedirect

from django.http import *
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy

from django.views.generic.detail import SingleObjectMixin
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.template import RequestContext

from django.contrib.auth.decorators import login_required

from EventsApp.models import Event
from EventsApp.forms import EventForm

import datetime
from django.utils import timezone
from django.contrib.auth.models import User
# Create your views here.

@login_required
def join(request, event_id):
    try:
        # already joined
        event = Event.objects.get(id=event_id, attendee=request.user)
        message = "You have already joined this event"
    except Event.DoesNotExist as e:
        # Event exist but joined
        try:
            event = Event.objects.get(id=event_id)
            event.attendee.add(request.user)
            event.save()
            message = "You have joined this event"
        except Event.DoesNotExist as e:
            message = "Error on event joining"

    event = Event.objects.get(id=event_id)
    joined = event.attendee.filter(id=request.user.id)
    return render(request, 'events/show.html', {
       'event': event,
       'message': message,
       'joined': joined
    })

@login_required
def cancel(request, event_id):
    try:
        event = Event.objects.get(id=event_id, attendee=request.user)
        event.attendee.remove(request.user)
        event.save()
        message = "Your request not to attend has been saved"
    except Event.DoesNotExist as e:
           message = "Error on cancelling your attedance on event"

    event = Event.objects.get(id=event_id)
    joined = event.attendee.filter(id=request.user.id)
    return render(request, 'events/show.html', {
        'event': event,
        'message': message,
        'joined': joined
    })


def user_event(request, user_id):
   try:
       event_list1 = Event.objects.filter(attendee__id=user_id)
       user1= User.objects.get(id=user_id)
       return render(request, 'events/user_event.html', {'event_list1': event_list1, 'user1': user1})
   except:
       event_list1 = []
       user1 = {}



def detail(request, id):
     event = Event.objects.get(id=id)
     joined = event.attendee.filter(id=request.user.id)
     return render(request, 'events/show.html', {'event': event, 'joined': joined})


class ShowEvents(generic.ListView):
    model = Event
    template_name = 'events/showall.html'
    context_object_name = 'event_list'


class ShowEvent(generic.DetailView):
    model = Event
    template_name = 'events/show.html'


class CreateEvent(generic.CreateView):
    form_class = EventForm
    model = Event
    template_name = 'events/create_form.html'

    def get_success_url(self):
        return reverse('EventsApp:ShowEvent', args=(self.object.id,))


class EditEvent(generic.UpdateView):
    form_class = EventForm
    model = Event
    template_name = 'events/edit_form.html'

    def get_success_url(self):
        return reverse('EventsApp:ShowEvent', args=(self.object.id,))


class DeleteEvent(generic.DeleteView):
    model = Event
    success_url = reverse_lazy('EventsApp:ShowEvents')

    def get(self, *args, **kwargs):
        raise Http404


