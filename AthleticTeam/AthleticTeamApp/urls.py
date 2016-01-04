from django.conf.urls import url

from . import views, rlviews

urlpatterns = [
    url(r'^coachingStaffMembers$', views.ShowCoachingStaffMembers.as_view(), name='ShowCoachingStaffMembers'),
    url(r'^coachingStaffMember/(?P<pk>[0-9]+)$', views.ShowCoachingStaffMember.as_view(), name='ShowCoachingStaffMember'),

    
    url(r'^matches$', views.ShowMatches.as_view(), name='ShowMatches'),
    url(r'^match/(?P<pk>[0-9]+)', views.ShowMatch.as_view(), name='ShowMatch'),
    
    url(r'^teams$', views.ShowTeams.as_view(), name='ShowTeams'),
    url(r'^create_team$', views.create_team, name='create_team'),
    url(r'^edit_team$', views.edit_team.as_view(), name='edit_team'),
    url(r'^edit_a_team$', views.edit_a_team, name='edit_a_team'),
    url(r'^EditTeam/(?P<pk>[0-9]+)$', views.EditTeam.as_view(), name='EditTeam'),
    url(r'^(?P<team_id>[0-9]+)/edit/$', views.edit, name='edit'),
    url(r'^team/(?P<pk>[0-9]+)$', views.ShowTeam.as_view(), name='ShowTeam'),

    url(r'^home/$', rlviews.HomeView.as_view(), name='home'),
    url(r'^$', rlviews.IndexView.as_view(), name='index'),
    url(r'^login/$', rlviews.login_user, name='login_user'),
    url(r'^logout/$', rlviews.logout_view, name='logout'),
    url(r'^about/$', rlviews.AboutUs.as_view(), name='about'),
    url(r'^profile/$', rlviews.ProfileView.as_view(), name='profile'),
    url(r'^change_info/$', rlviews.ChangePassView.as_view(), name='changePass'),
    url(r'^change_info_def/$', rlviews.change_pass, name='change_pass_def'),
    url(r'^ranking/(?P<pk>[0-9]+)$', rlviews.IndexRanking.as_view(), name='index_ranking'),
    url(r'^ranking/(?P<player_id>[0-9]+)/rank$', rlviews.rank, name='ranking'),
    url(r'^ranking_results/(?P<pk>[0-9]+)$', rlviews.RankingResults.as_view(), name='rank_results'),
    url(r'^ranking_results_view/(?P<player_id>[0-9]+)$', rlviews.get_rank, name='view_rank_player'),
    url(r'^first_rank/(?P<pk>[0-9]+)$', rlviews.FirstRank.as_view(), name='firstRank'),

    url(r'^teamPlays$', views.ShowTeamPlays.as_view(), name='ShowTeamPlays'),
    url(r'^teamPlay/create$', views.CreateTeamPlay.as_view(), name='CreateTeamPlay'),
    url(r'^teamPlay/(?P<pk>[0-9]+)$', views.ShowTeamPlay.as_view(), name='ShowTeamPlay'),
    url(r'^teamPlay/(?P<pk>[0-9]+)/edit$', views.EditTeamPlay.as_view(), name='EditTeamPlay'),
    url(r'^teamPlay/(?P<pk>[0-9]+)/delete$', views.DeleteTeamPlay.as_view(), name='DeleteTeamPlay'),

    url(r'^trainings$', views.ShowTrainings.as_view(), name='ShowTrainings'),
    url(r'^training/create$', views.CreateTraining.as_view(), name='CreateTraining'),
    url(r'^training/(?P<pk>[0-9]+)$', views.ShowTraining.as_view(), name='ShowTraining'),
    url(r'^training/(?P<pk>[0-9]+)/edit$', views.EditTraining.as_view(), name='EditTraining'),
    url(r'^training/(?P<pk>[0-9]+)/delete$', views.DeleteTraining.as_view(), name='DeleteTraining'),

    url(r'^exercises$', views.ShowExercises.as_view(), name='ShowExercises'),
    url(r'^exercise/create$', views.CreateExercise.as_view(), name='CreateExercise'),
    url(r'^exercise/(?P<pk>[0-9]+)$', views.ShowExercise.as_view(), name='ShowExercise'),
    url(r'^exercise/(?P<pk>[0-9]+)/edit$', views.EditExercise.as_view(), name='EditExercise'),
    url(r'^exercise/(?P<pk>[0-9]+)/delete$', views.DeleteExercise.as_view(), name='DeleteExercise'),
    
    url(r'^players$', views.ShowPlayers.as_view(), name='ShowPlayers'),
    url(r'^player/(?P<pk>[0-9]+)$', views.ShowPlayer.as_view(), name='ShowPlayer'),
    url(r'^edit_players$', views.edit_players.as_view(), name='edit_players'),
    url(r'^create_a_player$', views.create_a_player, name='create_a_player'),
    url(r'^create_player$', views.create_player.as_view(), name='create_player'),
    url(r'^edit_a_player$', views.edit_a_player, name='edit_a_player'),
    url(r'^EditPlayer/(?P<pk>[0-9]+)$', views.EditPlayer.as_view(), name='EditPlayer'),
    url(r'^(?P<player_id>[0-9]+)/edit_player/$', views.edit_player, name='edit_player'),
    url(r'^all_teams$', views.all_teams, name='all_teams'),
    url(r'^players_teams$', views.add_players_to_teams.as_view(), name='players_teams'),
   

    url(r'^create_match/$', views.CreateMatch.as_view(), name='CreateMatch'),
    url(r'^creating_match_stage_1/$', views.match_creator, name='match_stg1'),
    url(r'^edit_match/(?P<pk>[0-9]+)$', views.EditMatches.as_view(), name='EditMatch'),
    url(r'^edit_match_go_to_form/(?P<match_id>[0-9]+)$', views.edit_match, name='editmatch'),
    url(r'^match_edit/(?P<match_id>[0-9]+)$', views.match_edit, name='match_edit'),
    url(r'^player_stats/(?P<pk>[0-9]+)$', views.Players_stats.as_view(), name='Players_stats'),
    url(r'^all_stats/$', views.all_stats, name='all_stats'),

    url(r'^edit_match_stats/(?P<pk>[0-9]+)$', views.EditMatchStats.as_view(), name='EditMatchStats'),
    url(r'^match_stats/$', views.match_stats, name='match_stats'),
    url(r'^best_players/$', rlviews.ShowBestPlayers.as_view(), name='BestPlayers'),

    url(r'^leagues$', views.ShowLeagues.as_view(), name='ShowLeagues'),
    url(r'^league/create$', views.create_league, name='CreateLeague'),
    url(r'^league/(?P<pk>[0-9]+)$', views.ShowLeague.as_view(), name='ShowLeague'),
    url(r'^league/(?P<pk>[0-9]+)/edit$', views.edit_league, name='EditLeague'),
    url(r'^league/(?P<pk>[0-9]+)/edit_data$', views.edit_league_data, name='EditLeagueData'),
    url(r'^league/(?P<pk>[0-9]+)/delete$', views.DeleteLeague.as_view(), name='DeleteLeague'),

    url(r'^contact/$', views.contact, name='contact'),
    url(r'^organisationalCharts$', views.ShowOrganisationalCharts.as_view(), name='ShowOrganisationalCharts'),
    url(r'^organisationalChart/(?P<pk>[0-9]+)$', views.ShowOrganisationalChart.as_view(), name='ShowOrganisationalChart'),
    
]

