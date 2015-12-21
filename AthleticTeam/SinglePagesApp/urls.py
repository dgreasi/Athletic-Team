from django.conf.urls import url

from . import views

urlpatterns = [
   # url(r'^contactUs$', views.contact_us, name='contact_us'),
   # url(r'^contactUs/edit$', views.edit_contact_us, name='edit_contact_us'),
    url(r'^aboutUs$', views.about_us, name='about_us'),
    url(r'^aboutUs/edit$', views.edit_about_us, name='edit_about_us'),

    url(r'^history$', views.history, name='history'),
    url(r'^history/edit$', views.edit_history, name='edit_history'),
    url(r'^tickets$', views.tickets, name='tickets'),
    url(r'^tickets/edit$', views.edit_tickets, name='edit_tickets'),
    url(r'^events$', views.events, name='events'),
    url(r'^events/edit$', views.edit_events, name='edit_events'),
    url(r'^facilities$', views.facilities, name='facilities'),
    url(r'^facilities/edit$', views.edit_facilities, name='edit_facilities'),
    url(r'^sponsorships$', views.sponsorships, name='sponsorships'),
    url(r'^sponsorships/edit$', views.edit_sponsorships, name='edit_sponsorships'),

]