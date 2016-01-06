from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^sponsors$', views.ShowSponsors.as_view(), name='ShowSponsors'),
url(r'^sponsor/create$', views.CreateSponsor.as_view(), name='CreateSponsor'),
url(r'^sponsor/(?P<pk>[0-9]+)$', views.ShowSponsor.as_view(), name='ShowSponsor'),
url(r'^sponsor/(?P<pk>[0-9]+)/edit$', views.EditSponsor.as_view(), name='EditSponsor'),
url(r'^sponsor/(?P<pk>[0-9]+)/delete$', views.DeleteSponsor.as_view(), name='DeleteSponsor')
]