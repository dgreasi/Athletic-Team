from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^events$', views.ShowEvents.as_view(), name='ShowEvents'),
url(r'^event/create$', views.CreateEvent.as_view(), name='CreateEvent'),
url(r'^event/(?P<id>\d+)/$', 'EventsApp.views.detail', name='ShowEvent'),
url(r'^event/(?P<pk>[0-9]+)/edit$', views.EditEvent.as_view(), name='EditEvent'),
url(r'^event/(?P<pk>[0-9]+)/delete$', views.DeleteEvent.as_view(), name='DeleteEvent'),
url(r'^join/(?P<event_id>\d+)/$', 'EventsApp.views.join', name='event_join'),
url(r'^cancel/(?P<event_id>\d+)/$', 'EventsApp.views.cancel', name='event_cancel'),
url(r'^user_event/(?P<user_id>\d+)/$', 'EventsApp.views.user_event', name='user_event')
]