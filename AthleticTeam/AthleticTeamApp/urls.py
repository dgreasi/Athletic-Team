from django.conf.urls import url

from . import views, rlviews

urlpatterns = [
    url(r'^coachingStaffMembers$', views.ShowCoachingStaffMembers.as_view(), name='ShowCoachingStaffMembers'),
    url(r'^coachingStaffMember/(?P<pk>[0-9]+)$', views.ShowCoachingStaffMember.as_view(), name='ShowCoachingStaffMember'),
    url(r'^players$', views.ShowPlayers.as_view(), name='ShowPlayers'),
    url(r'^player/(?P<pk>[0-9]+)$', views.ShowPlayer.as_view(), name='ShowPlayer'),
    url(r'^matches$', views.ShowMatches.as_view(), name='ShowMatches'),
    url(r'^match/(?P<pk>[0-9]+)', views.ShowMatch.as_view(), name='ShowMatch'),
    url(r'^teams$', views.ShowTeams.as_view(), name='ShowTeams'),
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
    url(r'^create_match/$', views.CreateMatch.as_view(), name='CreateMatch'),
    url(r'^creating_match_stage_1/$', views.match_creator, name='match_stg1'),
    url(r'^edit_match/(?P<pk>[0-9]+)$', views.EditMatches.as_view(), name='EditMatch'),
    url(r'^edit_match_go_to_form/(?P<match_id>[0-9]+)$', views.edit_match, name='editmatch'),
    url(r'^match_edit/(?P<match_id>[0-9]+)$', views.match_edit, name='match_edit'),

    
]
