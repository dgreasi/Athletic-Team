from django.shortcuts import render, render_to_response, redirect,get_object_or_404
from django.views import generic

from AthleticTeamApp.models import Player, Match, CoachingStaffMember, Team, Ranking
from announcementsApp.models import Announcement
from django.contrib.auth.models import User

from django.http import *
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy

from django.views.generic.detail import SingleObjectMixin
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator

from django.utils import timezone



class IndexRanking(generic.DetailView):
    model = Player
    template_name = 'ranking/index.html'

    #U can come here only if u are logged in
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IndexRanking, self).dispatch(*args, **kwargs)

class RankingResults(generic.DetailView):
    model = Player
    template_name = 'ranking/results.html'
    #U can come here only if u are logged in
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(RankingResults, self).dispatch(*args, **kwargs)

class FirstRank(generic.DetailView):
    model = Player
    template_name = 'ranking/first_rank.html'
    #U can come here only if u are logged in
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FirstRank, self).dispatch(*args, **kwargs)


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
    else:
        return HttpResponseRedirect(reverse('AthleticTeamApp:home'))
    return HttpResponseRedirect(reverse('AthleticTeamApp:index'))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('AthleticTeamApp:index'))

class HomeView(generic.ListView):
    model = Announcement
    template_name = 'home/base_site.html'
    context_object_name = "announcement_list"
    paginate_by = 3

    def get_queryset(self):
        """
        Return all published Announcements (not including those set to be
        published in the future).
        """
        return Announcement.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')


class IndexView(TemplateView):
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
    if temp.count() > 0:
        p = temp.first()
        return HttpResponseRedirect(reverse('AthleticTeamApp:rank_results', args=(player_id,)))
    else:
        return HttpResponseRedirect(reverse('AthleticTeamApp:firstRank', args=(player_id,)))

def rank(request, player_id):
    print player_id
    player_ranked = get_object_or_404(Player, pk=player_id)
    owner_user = request.user
    userid = owner_user.id

    power_ranked_arm = int(float(request.POST['power_arm']))
    power_ranked_body = int(float(request.POST['power_body']))
    power_ranked_legs = int(float(request.POST['power_legs']))
    speed_ranked = int(float(request.POST['speed']))
    team_play_ranked = int(float(request.POST['team_play']))
    co_op_ranked = int(float(request.POST['co_op']))
    rate_of_pos_ranked = int(float(request.POST['rate_of_pos']))
    two_shots_ranked = int(float(request.POST['two_shots']))
    three_shots_ranked = int(float(request.POST['three_shots']))

    #checking if there is a rank for this player
    temp = Ranking.objects.filter(owner_id=userid, player_id=player_id)
    
    if temp.count() == 1 :
        #Edit
        print"EDITING RANK"
        pl_ranking = get_object_or_404(Ranking, owner_id=userid, player_id=player_id)
        pl_ranking.power_arm = power_ranked_arm
        pl_ranking.power_body = power_ranked_body
        pl_ranking.power_legs = power_ranked_legs
        pl_ranking.speed = speed_ranked
        pl_ranking.team_play = team_play_ranked
        pl_ranking.co_op = co_op_ranked
        pl_ranking.rate_of_pos = rate_of_pos_ranked
        pl_ranking.two_shots = two_shots_ranked
        pl_ranking.three_shots = three_shots_ranked

        pl_ranking.save()

        return HttpResponseRedirect(reverse('AthleticTeamApp:rank_results', args=(player_id,)))
    else:
        #create
        print"CREATING RANK"
        p = Ranking(player=player_ranked, owner=owner_user, power_arm=power_ranked_arm, power_body=power_ranked_body, power_legs=power_ranked_legs, speed=speed_ranked, team_play= team_play_ranked, co_op=co_op_ranked, rate_of_pos=rate_of_pos_ranked, two_shots=two_shots_ranked, three_shots=three_shots_ranked)
        
        p.save()

        return HttpResponseRedirect(reverse('AthleticTeamApp:rank_results', args=(player_id,)))

#check if user exists
def username_present(username):
    if User.objects.filter(username=username).exists():
        return True

    return False
