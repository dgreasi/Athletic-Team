from django.shortcuts import render, render_to_response, redirect,get_object_or_404
from django.views import generic

from AthleticTeamApp.models import Player, Match, CoachingStaffMember, Team, Ranking

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

class IndexRanking(generic.DetailView):
    model = Player
    template_name = 'ranking/index.html'

class RankingResults(generic.DetailView):
    model = Ranking
    template_name = 'ranking/results.html'

class FirstRank(generic.DetailView):
    model = Player
    template_name = 'ranking/first_rank.html'

def login_user(request):
    if 'login' in request.POST:
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
    elif 'visitor' in request.POST:
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
    #@method_decorator(login_required)
    #def dispatch(self, *args, **kwargs):
    #    return super(HomeView, self).dispatch(*args, **kwargs)

class IndexView(TemplateView):
    #model = User
    template_name = 'Login/index.html'

class AboutUs(TemplateView):
    template_name = 'home/about.html'


class ProfileView(TemplateView):
    template_name = 'home/profile.html'
    
    #U can come here only if u are logged in
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProfileView, self).dispatch(*args, **kwargs)


class ChangePassView(TemplateView):
    template_name = 'home/change_pass.html'

    #U can come here only if u are logged in
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ChangePassView, self).dispatch(*args, **kwargs)


def change_pass(request):
    logged_user = request.user
    text_a = request.POST['text_a']
    text_b = request.POST['text_b']

    if text_a == text_b:
        #change password
        logged_user.set_password(text_b) 
        logged_user.save()
        logout(request)
        return HttpResponseRedirect(reverse('AthleticTeamApp:index'))
    else:
        #prin error mesg MESSAGES DJANGO
        return HttpResponseRedirect(reverse('AthleticTeamApp:changePass'))

def get_rank(request, player_id):
    temp = Ranking.objects.filter(player_id=player_id)
    if temp.count() == 1:
        p = get_object_or_404(Ranking, player_id=player_id)
        return HttpResponseRedirect(reverse('AthleticTeamApp:rank_results', args=(p.id,)))
    else:
        return HttpResponseRedirect(reverse('AthleticTeamApp:firstRank', args=(player_id,)))

def rank(request, player_id):
    print player_id
    player_ranked = get_object_or_404(Player, pk=player_id)
    owner_user = request.user

    power_ranked = int(float(request.POST['power']))
    speed_ranked = int(float(request.POST['speed']))


    #checking if there is a rank for this player
    temp = Ranking.objects.filter(player_id=player_id)
    
    if temp.count() == 1:
        #Edit
        print"EDITING RANK"
        pl_ranking = get_object_or_404(Ranking, player_id=player_id)
        pl_ranking.power = power_ranked
        pl_ranking.speed = speed_ranked
        pl_ranking.save()
        return HttpResponseRedirect(reverse('AthleticTeamApp:rank_results', args=(pl_ranking.id,)))
    else:
        #create
        print"CREATING RANK"
        p = Ranking(player=player_ranked, owner=owner_user, power=power_ranked, speed=speed_ranked)
        p.save()
        return HttpResponseRedirect(reverse('AthleticTeamApp:rank_results', args=(p.id,)))


