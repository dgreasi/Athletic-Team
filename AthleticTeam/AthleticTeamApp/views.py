from django.shortcuts import render
from django.views import generic

from AthleticTeamApp.models import Player, Match, CoachingStaffMember, Team


# Create your views here.
class ShowCoachingStaffMembers(generic.ListView):
    model = CoachingStaffMember
    template_name = 'coaching_staff_member/showall.html'


class ShowCoachingStaffMember(generic.DetailView):
    model = CoachingStaffMember
    template_name = 'coaching_staff_member/show.html'


class ShowPlayers(generic.ListView):
    model = Player
    template_name = 'player/showall.html'


class ShowPlayer(generic.DetailView):
    model = Player
    template_name = 'player/show.html'


class ShowMatches(generic.ListView):
    model = Match
    template_name = 'match/showall.html'


class ShowMatch(generic.DetailView):
    model = Match
    template_name = 'match/show.html'


# Create your views here.
class ShowTeams(generic.ListView):
    model = Team
    template_name = 'team/showall.html'


class ShowTeam(generic.DetailView):
    model = Team
    template_name = 'team/show.html'    
