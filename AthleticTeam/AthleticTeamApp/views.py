from django.shortcuts import render, render_to_response, redirect,get_object_or_404
from django.views import generic

from AthleticTeamApp.models import Player, Match, CoachingStaffMember, Team, Ranking, TeamPlay, Exercise, Training
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

    new_first_name = request.POST['first_name']
    new_last_name = request.POST['last_name']
    #primary_position = request.POST['primary_position']
    #secondary_positions = request.POST['secondary_positions']
    new_number = request.POST['number']
    new_height = request.POST['height']
    new_weight = request.POST['weight']
    new_nationality = request.POST['nationality']
    
    temp = Player(first_name = new_first_name,team_id = selected_team.id)
    temp.last_name = new_last_name
    #temp.primary_position = primary_position
    #temp.secondary_positions = secondary_positions
    temp.number = new_number
    temp.height =new_height
    temp.weight = new_weight
    temp.nationality = new_nationality
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
    #primary_position = request.POST['primary_position']
    #secondary_positions = request.POST['secondary_positions']
    number = request.POST['number']
    height = request.POST['height']
    weight = request.POST['weight']
    nationality = request.POST['nationality']
    
    temp.first_name = first_name
    temp.last_name = last_name
    #temp.primary_position = primary_position
    #temp.secondary_positions = secondary_positions
    temp.number = number
    temp.height = height
    temp.weight = weight
    temp.nationality = nationality
    ##temp.announcement_text = text
    #temp.pub_date = timezone.now()
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


class DeleteTeamPlay(generic.DeleteView):
    model = TeamPlay
    success_url = reverse_lazy('AthleticTeamApp:ShowTeamPlays')
    template_name = 'team_play/edit_form.html'

    def get(self, *args, **kwargs):
        raise Http404


class ShowExercises(generic.ListView):
    model = Exercise
    template_name = 'exercise/showall.html'


class ShowExercise(generic.DetailView):
    model = Exercise
    template_name = 'exercise/show.html'


class CreateExercise(generic.CreateView):
    model = Exercise
    fields = ['name', 'duration', 'type', 'desc', 'obj']
    template_name = 'exercise/create_form.html'

    def get_success_url(self):
        return reverse('AthleticTeamApp:ShowExercise', args=(self.object.id,))


class EditExercise(generic.UpdateView):
    model = Exercise
    fields = ['name', 'duration', 'type', 'desc', 'obj']
    template_name = 'exercise/edit_form.html'

    def get_success_url(self):
        return reverse('AthleticTeamApp:ShowExercise', args=(self.object.id,))


class DeleteExercise(generic.DeleteView):
    model = Exercise
    success_url = reverse_lazy('AthleticTeamApp:ShowExercises')

    def get(self, *args, **kwargs):
        raise Http404


# Create your views here.
class ShowTrainings(generic.ListView):
    model = Training
    template_name = 'training/showall.html'


class ShowTraining(generic.DetailView):
    model = Training
    template_name = 'training/show.html'


class CreateTraining(generic.CreateView):
    model = Training
    fields = ['date', 'start', 'end', 'location', 'exercises', 'team_plays', 'team']
    template_name = 'training/create_form.html'

    def get_success_url(self):
        return reverse('AthleticTeamApp:ShowTraining', args=(self.object.id,))


class EditTraining(generic.UpdateView):
    model = Training
    fields = ['date', 'start', 'end', 'location', 'exercises', 'team_plays', 'team']
    template_name = 'training/edit_form.html'

    def get_success_url(self):
        return reverse('AthleticTeamApp:ShowTraining', args=(self.object.id,))


class DeleteTraining(generic.DeleteView):
    model = Training
    success_url = reverse_lazy('AthleticTeamApp:ShowExercises')

    def get(self, *args, **kwargs):
        raise Http404
