from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^matches$', views.ShowMatches.as_view(), name='ShowMatches'),
    url(r'^match/(?P<pk>[0-9]+)$', views.ShowMatch.as_view(), name='ShowMatch'),
]