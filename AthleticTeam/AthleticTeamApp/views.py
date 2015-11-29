from django.shortcuts import render, render_to_response, redirect
from django.views import generic

from AthleticTeamApp.models import Player, Match, CoachingStaffMember, Team
from django.http import *
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy

from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator

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

def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('AthleticTeamApp:home'))
    return HttpResponseRedirect(reverse('AthleticTeamApp:index'))

    #, context_instance=RequestContext(request)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('AthleticTeamApp:index'))

#@login_required(login_url='/login/')
#@method_decorator(login_required, name='login_user')
class HomeView(TemplateView):
    template_name = 'home/base_site.html'

    #U can come here only if u are logged in
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(HomeView, self).dispatch(*args, **kwargs)

class IndexView(TemplateView):
    #model = User
    template_name = 'Login/index.html'