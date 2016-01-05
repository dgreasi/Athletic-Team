from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^administrations$', views.ShowAdministrations.as_view(), name='ShowAdministrations'),
url(r'^administration/create$', views.CreateAdministration.as_view(), name='CreateAdministration'),
url(r'^administration/(?P<pk>[0-9]+)$', views.ShowAdministration.as_view(), name='ShowAdministration'),
url(r'^administration/(?P<pk>[0-9]+)/edit$', views.EditAdministration.as_view(), name='EditAdministration'),
url(r'^administration/(?P<pk>[0-9]+)/delete$', views.DeleteAdministration.as_view(), name='DeleteAdministration')
]