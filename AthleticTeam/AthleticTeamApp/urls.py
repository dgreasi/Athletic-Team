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
    url(r'^team/(?P<pk>[0-9]+)$', views.ShowTeam.as_view(), name='ShowTeam'),
	url(r'^home/$', views.HomeView.as_view(), name='home'),
	url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login/$', views.login_user, name='login_user'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^about/$', views.AboutUs.as_view(), name='about'),
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
    url(r'^change_info/$', views.ChangePassView.as_view(), name='changePass'),
    url(r'^change_info_def/$', views.change_pass, name='change_pass_def'),
    url(r'^ranking/(?P<pk>[0-9]+)$', views.IndexRanking.as_view(), name='index_ranking'),
    url(r'^ranking/(?P<player_id>[0-9]+)/rank$', views.rank, name='ranking'),
    url(r'^ranking_results/(?P<pk>[0-9]+)$', views.RankingResults.as_view(), name='rank_results'),
    url(r'^ranking_results_view/(?P<player_id>[0-9]+)$', views.get_rank, name='view_rank_player'),
    url(r'^first_rank/(?P<pk>[0-9]+)$', views.FirstRank.as_view(), name='firstRank'),

]
