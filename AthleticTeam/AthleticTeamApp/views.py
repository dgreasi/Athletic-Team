from django.shortcuts import render, render_to_response, redirect,get_object_or_404
from django.views import generic

from AthleticTeamApp.models import Player, Match, CoachingStaffMember, Team, Ranking, TeamPlay
from django.http import *
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy

from django.views.generic.detail import SingleObjectMixin
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator


# Create your views here.
class ShowCoachingStaffMembers(generic.ListView):
    model = CoachingStaffMember
    template_name = 'coaching_staff_member/showall.html'
    context_object_name = 'coachingstaffmember_list'


class ShowCoachingStaffMember(generic.DetailView):
    model = CoachingStaffMember
    template_name = 'coaching_staff_member/show.html'


class ShowPlayers(generic.ListView):
    model = Player
    template_name = 'player/showall.html'
    context_object_name = 'players_list'

class ShowPlayer(generic.DetailView):
    model = Player
    template_name = 'player/show.html'


class ShowMatches(generic.ListView):
    model = Match
    template_name = 'match/showall.html'
    context_object_name = 'matches_list'

class ShowMatch(generic.DetailView):
    model = Match
    template_name = 'match/show.html'


# Create your views here.
class ShowTeams(generic.ListView):
    model = Team
    template_name = 'team/showall.html'
    context_object_name = 'team_players_list'

class ShowTeam(generic.DetailView):
    model = Team
    template_name = 'team/show.html'


class ShowTeamPlays(generic.ListView):
    model = TeamPlay
    template_name = 'team_play/showall.html'


class ShowTeamPlay(generic.DetailView):
    model = TeamPlay
    template_name = 'team_play/show.html'


class CreateTeamPlay(generic.CreateView):
    model = TeamPlay
    fields = ['name', 'data']
    template_name = 'team_play/create_form.html'

    def get_success_url(self):
        return reverse('AthleticTeamApp:ShowTeamPlay', args=(self.object.id,))

class EditTeamPlay(generic.UpdateView):
    model = TeamPlay
    fields = ['name', 'data']
    template_name = 'team_play/edit_form.html'

    def get_success_url(self):
        return reverse('AthleticTeamApp:ShowTeamPlay', args=(self.object.id,))
