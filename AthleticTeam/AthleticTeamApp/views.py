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
from django.template import RequestContext



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

class add_players_to_teams(generic.ListView):
    model = Team
    template_name = 'player/player_team.html'
    context_object_name = 'teams_list'
    
def all_teams(request):
    players = request.POST.getlist('players')
    try :
      team = request.POST['teams']
    except (KeyError, Team.DoesNotExist):
        # Redisplay the Announcement voting form.
        return render(request, 'player/player_team.html', {
            'teams_list': Team.objects.all ,
            'error_message': "Oops you didn't select a Team. Please choose again",
        })
    else:  
      print "Team:" + team
      print  players
      for player in players:
	
	temp = get_object_or_404(Player, pk=player)
	temp.team = Team.objects.get(id=team)
	temp.save()
      
      return HttpResponseRedirect(reverse('AthleticTeamApp:ShowPlayers'))
  
def create_a_player(request):     
    p = Team.objects.all()
    selected_team = get_object_or_404(Team, pk=request.POST['team'])
    #form = ImageUploadForm(request.POST, request.FILES)
    
    new_first_name = request.POST['first_name']
    new_last_name = request.POST['last_name']
    new_primary_position = request.POST.get('thesi',False)
    new_secondary_positions = request.POST.getlist('secondary_positions')
    new_number = request.POST['number']
    new_height = request.POST['height']
    new_weight = request.POST['weight']
    new_nationality = request.POST['nationality']
    new_birth_date = request.POST['date']
    new_photo = request.FILES['image']
    
    temp = Player(first_name = new_first_name,team_id = selected_team.id)
    temp.last_name = new_last_name
    temp.primary_position = new_primary_position
    temp.secondary_positions = '/'.join(new_secondary_positions)
    temp.number = new_number
    temp.height =new_height
    temp.weight = new_weight
    temp.nationality = new_nationality
    temp.birth_date = new_birth_date
    temp.image =new_photo 
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

    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    new_primary_position = request.POST.get('thesi',False)
    new_secondary_positions = request.POST.getlist('secondary_positions')
    number = request.POST['number']
    height = request.POST['height']
    weight = request.POST['weight']
    nationality = request.POST['nationality']
    new_birth_date = request.POST['date']
    new_photo = request.FILES['image']
    
    temp.first_name = first_name
    temp.last_name = last_name
    temp.primary_position = new_primary_position
    temp.secondary_positions = '/'.join(new_secondary_positions)
    temp.number = number
    temp.height = height
    temp.weight = weight
    temp.nationality = nationality
    temp.birth_date= new_birth_date
    temp.image =new_photo
    temp.save()

    return HttpResponseRedirect(reverse('AthleticTeamApp:ShowPlayers'))  

	  
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
    new_photo = request.FILES['image']
    temp = Team(team_name=title)
    temp.image =new_photo
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
    new_photo = request.FILES['image']
    
    temp.team_name = title
    temp.image =new_photo
    #temp.pub_date = timezone.now()
    temp.save()

    return HttpResponseRedirect(reverse('AthleticTeamApp:ShowTeams'))

    #return HttpResponseRedirect(reverse('AthleticTeamApp:ShowTeams'))

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
