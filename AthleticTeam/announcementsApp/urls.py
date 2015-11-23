from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^full/$', views.FullView.as_view(), name='full'),
    url(r'^announce/$', views.announce, name='announce'),
    url(r'^(?P<announcement_id>[0-9]+)/delete/$', views.delete, name='delete'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<announcement_id>[0-9]+)/comment/$', views.comment, name='comment'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<announcement_id>[0-9]+)/vote/$', views.vote, name='vote'),
]