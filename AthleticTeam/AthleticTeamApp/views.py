from django.shortcuts import render
from django.views import generic
from AthleticTeamApp.models import Player, Match,Training


# Create your views here.
class ShowPlayers(generic.ListView):
    model = Player
    template_name = 'player/showall.html'


class ShowPlayer(generic.DetailView):
    model = Player
    template_name = 'player/show.html'


# Create your views here.
class ShowMatches(generic.ListView):
    model = Match
    template_name = 'match/showall.html'


class ShowMatch(generic.DetailView):
    model = Match
    template_name = 'match/show.html'

# Create your views here.
class ShowTrainings(generic.ListView):
    model = Training
    template_name = 'training/showall.html'


class ShowTraining(generic.DetailView):
    model = Training
    template_name = 'training/show.html'