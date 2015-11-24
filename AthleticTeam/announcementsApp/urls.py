from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^full/$', views.FullView.as_view(), name='full'),

    url(r'^announce/$', views.announce, name='announce'),
    url(r'^myannouncements/$', views.MyannouncementsView.as_view(), name='myannouncements'),

    url(r'^(?P<pk>[0-9]+)/edit_announcement/$', views.EditAnnView.as_view(), name='edit_announcement'),
    url(r'^deleteAnnouncement/$', views.deleteAnnouncement, name='deleteAnnouncement'),
    url(r'^(?P<announcement_id>[0-9]+)/edit_announce/$', views.edit_announce, name='edit_announce'),
    
    
    url(r'^(?P<announcement_id>[0-9]+)/delete/$', views.delete, name='delete'),
    url(r'^(?P<announcement_id>[0-9]+)/edit_comment/$', views.MyeditcommentView.as_view, name='edit_comment'),
    
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    
    url(r'^(?P<announcement_id>[0-9]+)/comment/$', views.comment, name='comment'),
    
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<announcement_id>[0-9]+)/vote/$', views.vote, name='vote'),
]