from django.shortcuts import render
from django.views import generic
from AthleticTeamApp.models import Match


# Create your views here.
class ShowMatches(generic.ListView):
    model = Match
    template_name = 'match/showall.html'


class ShowMatch(generic.DetailView):
    model = Match
    template_name = 'match/show.html'