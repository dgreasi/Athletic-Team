from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^coachingStaffMembers$', views.ShowCoachingStaffMembers.as_view(), name='ShowCoachingStaffMembers'),
    url(r'^coachingStaffMember/(?P<pk>[0-9]+)$', views.ShowCoachingStaffMember.as_view(), name='ShowCoachingStaffMember'),

    url(r'^players$', views.ShowPlayers.as_view(), name='ShowPlayers'),
    url(r'^player/(?P<pk>[0-9]+)$', views.ShowPlayer.as_view(), name='ShowPlayer'),

    url(r'^matches$', views.ShowMatches.as_view(), name='ShowMatches'),
    url(r'^match/(?P<pk>[0-9]+)$', views.ShowMatch.as_view(), name='ShowMatch'),

    url(r'^teams$', views.ShowTeams.as_view(), name='ShowTeams'),
    url(r'^team/(?P<pk>[0-9]+)$', views.ShowTeam.as_view(), name='ShowTeam'),

    url(r'^teamPlays$', views.ShowTeamPlays.as_view(), name='ShowTeamPlays'),
    url(r'^teamPlay/create$', views.CreateTeamPlay.as_view(), name='CreateTeamPlay'),
    url(r'^teamPlay/(?P<pk>[0-9]+)$', views.ShowTeamPlay.as_view(), name='ShowTeamPlay'),
    url(r'^teamPlay/(?P<pk>[0-9]+)/edit$', views.EditTeamPlay.as_view(), name='EditTeamPlay'),

    url(r'^home/$', views.HomeView.as_view(), name='home'),
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^login/$', views.login_user, name='login_user'),
    url(r'^logout/$', views.logout_view, name='logout'),
]
