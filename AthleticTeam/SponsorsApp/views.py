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

from SponsorsApp.models import Sponsor
from .forms import UploadImageForm

# Create your views here.


class ShowSponsors(generic.ListView):
    model = Sponsor
    template_name = 'sponsor/showall.html'
    context_object_name = 'sponsor_list'


class ShowSponsor(generic.DetailView):
    model = Sponsor
    template_name = 'sponsor/show.html'


class CreateSponsor(generic.CreateView):
    model = Sponsor
    fields = ['name', 'info']
    template_name = 'sponsor/create_form.html'

    def get_success_url(self):
        return reverse('SponsorsApp:ShowSponsor', args=(self.object.id,))


class EditSponsor(generic.UpdateView):
    model = Sponsor
    fields = ['name', 'info']
    template_name = 'sponsor/edit_form.html'

    def get_success_url(self):
        return reverse('SponsorsApp:ShowSponsor', args=(self.object.id,))


class DeleteSponsor(generic.DeleteView):
    model = Sponsor
    success_url = reverse_lazy('SponsorsApp:ShowSponsors')

    def get(self, *args, **kwargs):
        raise Http404


