from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^contactUs$', views.contact_us, name='contact_us'),
    url(r'^contactUs/edit$', views.edit_contact_us, name='edit_contact_us'),
]