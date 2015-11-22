from django.shortcuts import render
from django.views import generic
from AthleticTeamApp.models import Player


# Create your views here.
class ShowPlayers(generic.ListView):
    model = Player
    template_name = 'player/showall.html'


class ShowPlayer(generic.DetailView):
    model = Player
    template_name = 'player/show.html'
