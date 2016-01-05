from django.forms import modelform_factory
from django.shortcuts import render, render_to_response, redirect,get_object_or_404
from django.views import generic

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


from AdministrationApp.models import Administration
# Create your views here.


class ShowAdministrations(generic.ListView):
    model = Administration
    template_name = 'showall.html'
    context_object_name = 'administration_list'


class ShowAdministration(generic.DetailView):
    model = Administration
    template_name = 'show.html'


class CreateAdministration(generic.CreateView):
    model = Administration
    fields = ['first_name', 'last_name', 'position', 'profile', 'nationality']
    template_name = 'create_form.html'

    def get_success_url(self):
        return reverse('AdministrationApp:ShowAdministration', args=(self.object.id,))


class EditAdministration(generic.UpdateView):
    model = Administration
    fields = ['first_name', 'last_name', 'position', 'profile', 'nationality']
    template_name = 'edit_form.html'

    def get_success_url(self):
        return reverse('AdministrationApp:ShowAdministration', args=(self.object.id,))


class DeleteAdministration(generic.DeleteView):
    model = Administration
    success_url = reverse_lazy('AdministrationApp:ShowAdministrations')

    def get(self, *args, **kwargs):
        raise Http404


