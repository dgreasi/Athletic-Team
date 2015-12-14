from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^contactUs$', views.contact_us, name='contact_us'),
    url(r'^contactUs/edit$', views.edit_contact_us, name='edit_contact_us'),
    url(r'^aboutUs$', views.about_us, name='about_us'),
    url(r'^aboutUs/edit$', views.edit_about_us, name='edit_about_us'),
    url(r'^sponsorships$', views.sponsorships, name='sponsorships'),
    url(r'^sponsorships/edit$', views.edit_sponsorships, name='edit_sponsorships'),
]