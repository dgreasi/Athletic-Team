from django.shortcuts import render, render_to_response, redirect,get_object_or_404
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
    context_object_name = 'coachingstaffmember_list'


class ShowCoachingStaffMember(generic.DetailView):
    model = CoachingStaffMember
    template_name = 'coaching_staff_member/show.html'

##################
# Players Views.
##################
class ShowPlayers(generic.ListView):
    model = Player
    template_name = 'player/showall.html'
    context_object_name = 'players_list'

#def create_player(request):
    #title = request.POST['title']
    ##temp = Player(first_name = title,team_id = 22)
   ##temp.save()
    
    #return HttpResponseRedirect(reverse('AthleticTeamApp:ShowPlayers'))

class ShowPlayer(generic.DetailView):
    model = Player
    template_name = 'player/show.html'


class create_player(generic.ListView):  
    #title = request.POST['title']
    #temp = Team(team_name=title)
    #temp.save()
    model = Team
    template_name = 'player/create_player.html'
    context_object_name = 'teams_list'   
    
class edit_players(generic.ListView):
    model = Player
    template_name = 'player/edit_players.html'
    context_object_name = 'players_list'
   
class EditPlayer(generic.DetailView):
    model = Player
    template_name = 'player/edit.html'
   
   
def create_a_player(request):     
    p = Team.objects.all()
    selected_team = get_object_or_404(Team, pk=request.POST['team'])
    title = request.POST['title']
    temp = Player(first_name = title,team_id = selected_team.id)
    temp.save()

    return HttpResponseRedirect(reverse('AthleticTeamApp:ShowPlayers'))
  
def edit_a_player(request):     
    p = Player.objects.all()
    selected_player = get_object_or_404(Player, pk=request.POST['player'])
    if 'delete' in request.POST:
      selected_player.delete()
            ## Always return an HttpResponseRedirect after successfully dealing
            ## with POST data. This prevents data from being posted twice if a
            ## user hits the Back button.
      return  HttpResponseRedirect(reverse('AthleticTeamApp:ShowPlayers'))
    elif 'edit' in request.POST:  
      return HttpResponseRedirect(reverse('AthleticTeamApp:EditPlayer',args=(selected_player.id,))) 
    
def edit_player(request,player_id):
    temp = get_object_or_404(Player, pk=player_id)

    title = request.POST['title']
    #text = request.POST['text']
    
    temp.first_name = title
    ##temp.announcement_text = text
    #temp.pub_date = timezone.now()
    temp.save()

    return HttpResponseRedirect(reverse('AthleticTeamApp:ShowPlayers'))

    #return HttpResponseRedirect(reverse('AthleticTeamApp:ShowTeams'))    
  
	  
##################
# Matches Views.
##################

class ShowMatches(generic.ListView):
    model = Match
    template_name = 'match/showall.html'
    context_object_name = 'matches_list'

class ShowMatch(generic.DetailView):
    model = Match
    template_name = 'match/show.html'

##################
# Teams Views.
##################
class ShowTeams(generic.ListView):
    model = Team
    template_name = 'team/showall.html'
    context_object_name = 'team_players_list'
    
def create_team(request):
    title = request.POST['title']
    temp = Team(team_name=title)
    temp.save()

    return HttpResponseRedirect(reverse('AthleticTeamApp:ShowTeams'))

class edit_team(generic.ListView):  
    #title = request.POST['title']
    #temp = Team(team_name=title)
    #temp.save()
    model = Team
    template_name = 'team/edit_team.html'
    context_object_name = 'team_players_list'

def edit_a_team(request):     
    p = Team.objects.all()
    selected_team = get_object_or_404(Team, pk=request.POST['team'])
    if 'delete' in request.POST:
      selected_team.delete()
            ## Always return an HttpResponseRedirect after successfully dealing
            ## with POST data. This prevents data from being posted twice if a
            ## user hits the Back button.
      return  HttpResponseRedirect(reverse('AthleticTeamApp:ShowTeams'))
    elif 'edit' in request.POST:  
      return HttpResponseRedirect(reverse('AthleticTeamApp:EditTeam',args=(selected_team.id,)))

class EditTeam(generic.DetailView):
    model = Team
    template_name = 'team/edit.html'
	  
def edit(request,team_id):
    temp = get_object_or_404(Team, pk=team_id)

    title = request.POST['title']
    #text = request.POST['text']
    
    temp.team_name = title
    ##temp.announcement_text = text
    #temp.pub_date = timezone.now()
    temp.save()

    return HttpResponseRedirect(reverse('AthleticTeamApp:ShowTeams'))

    #return HttpResponseRedirect(reverse('AthleticTeamApp:ShowTeams'))

class ShowTeam(generic.DetailView):
    model = Team
    template_name = 'team/show.html'

class IndexRanking(TemplateView):
    template_name = 'ranking/index.html'

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
