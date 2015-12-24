from django.forms import modelform_factory
from django.shortcuts import render, render_to_response, redirect,get_object_or_404
from django.views import generic

from AthleticTeamApp.forms import TrainingForm
from AthleticTeamApp.models import Player, Match, CoachingStaffMember, Team, Ranking, TeamPlay, Exercise, Training, MatchPlayerStatistics

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
import datetime
from django.utils import timezone


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
    if 'image' in request.FILES:
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
    if 'image' in request.FILES:
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
    if 'image' in request.FILES:
      new_photo = request.FILES['image']
    
    temp.first_name = first_name
    temp.last_name = last_name
    temp.primary_position = new_primary_position
    temp.secondary_positions = '/'.join(new_secondary_positions)
    temp.number = int(number)
    temp.height = height
    temp.weight = int(weight)
    temp.nationality = nationality
    temp.birth_date = new_birth_date
    if 'image' in request.FILES: 
      temp.image = new_photo
    temp.save()

    return HttpResponseRedirect(reverse('AthleticTeamApp:ShowPlayers'))  

	  
##################
# Matches Views.
##################

class ShowMatches(generic.ListView):
    model = Match
    template_name = 'match/showall.html'
    context_object_name = 'matches_list'
    paginate_by = 3

    def get_queryset(self):
        """
        Return order_by date).
        """
        return Match.objects.filter(date__lte=timezone.now()).order_by('-date')

class EditMatches(generic.DetailView):
    model = Match
    template_name = 'match/edit_match.html'
        

class ShowMatch(generic.DetailView):
    model = Match
    template_name = 'match/show.html'
    
class EditMatchStats(generic.DetailView):
    model = Match
    template_name = 'match/edit_match_stats.html'    


##################
# Teams Views.
##################
# Create your views here.
class ShowTeams(generic.ListView):
    model = Team
    template_name = 'team/showall.html'
    context_object_name = 'team_players_list'
    
def create_team(request):
    title = request.POST['title']
    if 'image' in request.FILES:
      new_photo = request.FILES['image']
    temp = Team(team_name=title)
    if 'image' in request.FILES:
      temp.image = new_photo
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
    if 'image' in request.FILES:
      new_photo = request.FILES['image']
    
    temp.team_name = title
    if 'image' in request.FILES:  
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
    form_class = TrainingForm
    model = Training
    template_name = 'training/create_form.html'

    def get_success_url(self):
        return reverse('AthleticTeamApp:ShowTraining', args=(self.object.id,))


class EditTraining(generic.UpdateView):
    form_class = TrainingForm
    model = Training
    template_name = 'training/edit_form.html'

    def get_success_url(self):
        return reverse('AthleticTeamApp:ShowTraining', args=(self.object.id,))


class DeleteTraining(generic.DeleteView):
    model = Training
    success_url = reverse_lazy('AthleticTeamApp:ShowTrainings')

    def get(self, *args, **kwargs):
        raise Http404

##################
# Match Views.
##################
class CreateMatch(generic.ListView):
    model = Team
    template_name = 'match/create_match.html'
    context_object_name = "teams_list"

def match_creator(request):
    team_a_id = request.POST['team_a']
    team_a = get_object_or_404(Team, pk=team_a_id)

    team_b = request.POST['team_b']

    points_a = int(request.POST.get('points_a', False))
    points_b = int(request.POST.get('points_b', False))

    date_match = request.POST['date_match']
    time_match = request.POST['time_match']
    stadium = request.POST['stadium']
    info = request.POST['info']

    home_away_team = request.POST['home_away']

    match_to_send = Match(home_pts=points_a, away_pts=points_b, stadium=stadium, date=date_match, time=time_match, info=info, home_team=team_a, away_team=team_b, home_away=home_away_team)

    match_to_send.save()  

    # list1 = Player.objects.filter(team=team_a)

    # for p in list1:
    #     temp = MatchPlayerStatistics(match=match_to_send, player=p, started=1)
    #     temp.save()

    return HttpResponseRedirect(reverse('AthleticTeamApp:Players_stats', args=(match_to_send.id,)))

def match_edit(request, match_id):
    match_to_edit = get_object_or_404(Match, pk=match_id)

    team_a_id = request.POST['team_a']
    team_a = get_object_or_404(Team, pk=team_a_id)
    team_b = request.POST['team_b']
    points_a = int(request.POST.get('points_a', False))
    points_b = int(request.POST.get('points_b', False))
    date_match = request.POST['date_match']
    time_match = request.POST['time_match']
    stadium = request.POST['stadium']
    info = request.POST['info']
    home_away_team = request.POST['home_away']

    # EDIT FIELDS
    match_to_edit.home_pts = points_a
    match_to_edit.away_pts = points_b
    match_to_edit.stadium = stadium
    match_to_edit.date = date_match
    match_to_edit.time = time_match
    match_to_edit.info = info
    match_to_edit.home_team = team_a
    match_to_edit.away_team = team_b
    match_to_edit.home_away = home_away_team

    match_to_edit.save()  

    return HttpResponseRedirect(reverse('AthleticTeamApp:ShowMatches'))

def edit_match(request, match_id):
    selected_match = get_object_or_404(Match, pk=match_id)

    if 'edit' in request.POST:
        return HttpResponseRedirect(reverse('AthleticTeamApp:EditMatch', args=(selected_match.id,)))
    elif 'edit_stats' in request.POST:
	return HttpResponseRedirect(reverse('AthleticTeamApp:EditMatchStats', args=(selected_match.id,)))
    elif 'delete' in request.POST:
        selected_match.delete()
        return HttpResponseRedirect(reverse('AthleticTeamApp:ShowMatches'))

class Players_stats(generic.DetailView):
    model = Match
    template_name = 'match/players_stats.html'
    
def all_stats(request):
  
  agwnas = request.POST['match']
  name1 = request.POST.getlist('player1')
  name2 = request.POST.getlist('player2')
  minutes = request.POST.getlist('min')
  two_a = request.POST.getlist('2pt-a')
  two_m = request.POST.getlist('2pt_m')
  threept_a = request.POST.getlist('3pt-a')
  threept_m = request.POST.getlist('3pt-m')
  f_a = request.POST.getlist('f-a')
  f_m = request.POST.getlist('f-m')
  to = request.POST.getlist('to')
  off = request.POST.getlist('off')
  defreb = request.POST.getlist('def')
  blk = request.POST.getlist('blk')
  pf = request.POST.getlist('pf')
  pts = request.POST.getlist('pts')
  player = request.POST.getlist('players')
  ass = request.POST.getlist('ass')
  st = request.POST.getlist('st')
  
  
  for i in range(len(name1)):
    
    paiktis = Player.objects.get(first_name = name1[i] , last_name = name2[i]) 
    match1 = Match.objects.get(pk = agwnas)  
    temp = MatchPlayerStatistics(match=match1 ,player=paiktis,started=1)
    temp.time_played = int(minutes[i]) 
    temp.pts = int(pts[i])
    temp.two_pa = int(two_a[i])
    temp.two_pm = int(two_m[i])
    temp.three_pa = int(threept_a[i])
    temp.three_pm = int(threept_m[i])
    temp.fta = int(f_a[i])
    temp.ftm = int(f_m[i])
    temp.tov = int(to[i])
    temp.oreb = int(off[i])
    temp.dreb = int(defreb[i])
    temp.ast = int(ass[i])
    temp.stl = int(st[i])
    temp.blk = int(blk[i])
    temp.pf = int(pf[i])
    
    temp.save()

  return HttpResponseRedirect(reverse('AthleticTeamApp:ShowMatches'))

def match_stats(request):
  
  agwnas = request.POST['match1']
  paiktis = request.POST.getlist('player')
  minutes = request.POST.getlist('time_played')
  two_a = request.POST.getlist('two_pa')
  two_m = request.POST.getlist('two_pm')
  threept_a = request.POST.getlist('three_pa')
  threept_m = request.POST.getlist('three_pm')
  f_a = request.POST.getlist('fta')
  f_m = request.POST.getlist('ftm')
  to = request.POST.getlist('tov')
  off = request.POST.getlist('oreb')
  defreb = request.POST.getlist('dreb')
  blk = request.POST.getlist('blk')
  pf = request.POST.getlist('pf')
  pts = request.POST.getlist('pts')
  ass = request.POST.getlist('ast')
  st = request.POST.getlist('stl')
  
  
  for i in range(len(paiktis)):
    
    paiktis1 = Player.objects.get(pk = paiktis[i]) 
    #temp = MatchPlayerStatistics(match=match1 ,player=paiktis,started=1)
    temp = get_object_or_404(MatchPlayerStatistics, match=agwnas ,player=paiktis1)
    temp.time_played = int(minutes[i]) 
    temp.pts = int(pts[i])
    temp.two_pa = int(two_a[i])
    temp.two_pm = int(two_m[i])
    temp.three_pa = int(threept_a[i])
    temp.three_pm = int(threept_m[i])
    temp.fta = int(f_a[i])
    temp.ftm = int(f_m[i])
    temp.tov = int(to[i])
    temp.oreb = int(off[i])
    temp.dreb = int(defreb[i])
    temp.ast = int(ass[i])
    temp.stl = int(st[i])
    temp.blk = int(blk[i])
    temp.pf = int(pf[i])
    
    temp.save()

  return HttpResponseRedirect(reverse('AthleticTeamApp:ShowMatches'))
