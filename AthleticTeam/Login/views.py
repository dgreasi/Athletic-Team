from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.views.generic import TemplateView


# Create your views here.
class IndexView(TemplateView):
	#model = User
	template_name = 'Login/index.html'

class HomeView(TemplateView):
	template_name = 'Login/base_site.html'

