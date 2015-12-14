import json as simplejson
from django.http import Http404
from django.shortcuts import render, redirect
# Create your views here.
from AthleticTeam.settings import MEDIA_ROOT
from SinglePagesApp.forms import EditContactUsForm, EditAboutUsForm, EditSponsorshipsForm
#from SinglePagesApp.forms import EditAboutUsForm


def sponsorships(request):
    data = read_file('sponsorships.json')

    if data['visible'] != '':
        return render(request, 'single_pages/sponsorships.html', context={'data': data})
    else:
        raise Http404("Contact Us Page isn't used")


def about_us(request):
    data = read_file('about_us.json')

    if data['visible'] != '':
        return render(request, 'single_pages/about_us.html', context={'data': data})
    else:
        raise Http404("About Us Page isn't used")


def contact_us(request):
    data = read_file('contact_us.json')

    if data['visible'] != '':
        return render(request, 'single_pages/contact_us.html', context={'data': data})
    else:
        raise Http404("Contact Us Page isn't used")


def edit_sponsorships(request):
    if request.method == 'POST':
        data = request.POST
        data = data.copy()
        data.pop('csrfmiddlewaretoken', None)
        write_file('sponsorships.json', data)
        return redirect('SinglePagesApp:sponsorships')
    else:
        name = 'sponsorships'
        data = read_file('sponsorships.json')
        form = EditSponsorshipsForm(data)
        return render(request, 'single_pages/edit.html', context={'name': name, 'form': form})


def edit_about_us(request):
    if request.method == 'POST':
        data = request.POST
        data = data.copy()
        data.pop('csrfmiddlewaretoken', None)
        write_file('about_us.json', data)
        return redirect('SinglePagesApp:about_us')
    else:
        name = 'About Us'
        data = read_file('about_us.json')
        form = EditAboutUsForm(data)
        return render(request, 'single_pages/edit.html', context={'name': name, 'form': form})

def edit_contact_us(request):
    if request.method == 'POST':
        data = request.POST
        data = data.copy()
        data.pop('csrfmiddlewaretoken', None)
        write_file('contact_us.json', data)
        return redirect('SinglePagesApp:contact_us')
    else:
        name = 'Contact Us'
        data = read_file('contact_us.json')
        form = EditContactUsForm(data)
        return render(request, 'single_pages/edit.html', context={'name': name, 'form': form})


def read_file(file_name):
    file_handler = open(MEDIA_ROOT + './SinglePagesData/' + file_name, mode='r')
    data = simplejson.load(file_handler)  # deserialises it
    file_handler.close()
    return data


def write_file(file_name, data):
    file_handler = open(MEDIA_ROOT + './SinglePagesData/' + file_name, mode='w')
    data = simplejson.dumps(data)
    file_handler.write(data)
    file_handler.close()

