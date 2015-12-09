from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^coachingStaffMembers$', views.ShowCoachingStaffMembers.as_view(), name='ShowCoachingStaffMembers'),
    url(r'^coachingStaffMember/(?P<pk>[0-9]+)$', views.ShowCoachingStaffMember.as_view(), name='ShowCoachingStaffMember'),
    url(r'^players$', views.ShowPlayers.as_view(), name='ShowPlayers'),
    url(r'^player/(?P<pk>[0-9]+)$', views.ShowPlayer.as_view(), name='ShowPlayer'),
    url(r'^matches$', views.ShowMatches.as_view(), name='ShowMatches'),
    url(r'^match/(?P<pk>[0-9]+)', views.ShowMatch.as_view(), name='ShowMatch'),
    
    url(r'^teams$', views.ShowTeams.as_view(), name='ShowTeams'),
    url(r'^create_team$', views.create_team, name='create_team'),
    url(r'^edit_team$', views.edit_team.as_view(), name='edit_team'),
    url(r'^edit_a_team$', views.edit_a_team, name='edit_a_team'),
    url(r'^EditTeam/(?P<pk>[0-9]+)$', views.EditTeam.as_view(), name='EditTeam'),
    url(r'^(?P<team_id>[0-9]+)/edit/$', views.edit, name='edit'),
    #url(r'^(?P<announcement_id>[0-9]+)/edit_announce/$', views.edit_announce, name='edit_announce'),
    url(r'^add_players$', views.add_players, name='add_players'),
    url(r'^team/(?P<pk>[0-9]+)$', views.ShowTeam.as_view(), name='ShowTeam'),
	url(r'^home/$', views.HomeView.as_view(), name='home'),
	url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login/$', views.login_user, name='login_user'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^about/$', views.AboutUs.as_view(), name='about'),
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
    url(r'^change_info/$', views.ChangePassView.as_view(), name='changePass'),
    url(r'^change_info_def/$', views.change_pass, name='change_pass_def'),
    url(r'^ranking/$', views.IndexRanking.as_view(), name='index_ranking'),
]
