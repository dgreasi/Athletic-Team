import json

from django.http import Http404
from django.shortcuts import render, redirect
# Create your views here.
from AthleticTeam.settings import MEDIA_ROOT
from SinglePagesApp.forms import EditContactUsForm, EditHistoryForm, EditTicketsForm, EditFacilitiesForm

def history(request):
    data = read_file('history.json')

    if data['visible'] != '':
        return render(request, 'single_pages/history.html', context={'data': data})
    else:
        raise Http404("History Page isn't used")


def edit_history(request):
    if request.method == 'POST':
        data = request.POST
        data = data.copy()
        data.pop('csrfmiddlewaretoken', None)
        write_file('history.json', data)
        return redirect('SinglePagesApp:history')
    else:
        name = 'history'
        data = read_file('history.json')
        form = EditHistoryForm(data)
        return render(request, 'single_pages/edit.html', context={'name': name, 'form': form})


def contact_us(request):
    data = read_file('contact_us.json')

    if data['visible'] != '':
        return render(request, 'single_pages/contact_us.html', context={'data': data})
    else:
        raise Http404("Contact Us Page isn't used")

def about_us(request):
    data = read_file('about_us.json')

    if data['visible'] != '':
        return render(request, 'single_pages/about_us.html', context={'data': data})
    else:
        raise Http404("About Us Page isn't used")


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
    data = json.load(file_handler)  # deserialises it
    file_handler.close()
    return data


def write_file(file_name, data):
    file_handler = open(MEDIA_ROOT + './SinglePagesData/' + file_name, mode='w')
    data = json.dumps(data)
    file_handler.write(data)
    file_handler.close()

def tickets(request):
    data = read_file('tickets.json')

    if data['visible'] != '':
        return render(request, 'single_pages/tickets.html', context={'data': data})
    else:
        raise Http404("Tickets Page isn't used")

def edit_tickets(request):
    if request.method == 'POST':
        data = request.POST
        data = data.copy()
        data.pop('csrfmiddlewaretoken', None)
        write_file('tickets.json', data)
        return redirect('SinglePagesApp:tickets')
    else:
        name = 'Tickets'
        data = read_file('tickets.json')
        form = EditTicketsForm(data)
        return render(request, 'single_pages/edit.html', context={'name': name, 'form': form})

def events(request):
    data = read_file('events.json')

    if data['visible'] != '':
        return render(request, 'single_pages/events.html', context={'data': data})
    else:
        raise Http404("events Page isn't used")


def edit_events(request):
    if request.method == 'POST':
        data = request.POST
        data = data.copy()
        data.pop('csrfmiddlewaretoken', None)
        write_file('events.json', data)
        return redirect('SinglePagesApp:events')
    else:
        name = 'events'
        data = read_file('events.json')
        form = EditHistoryForm(data)
        return render(request, 'single_pages/edit.html', context={'name': name, 'form': form})

def facilities(request):
    data = read_file('facilities.json')

    if data['visible'] != '':
        return render(request, 'single_pages/facilities.html', context={'data': data})
    else:
        raise Http404("Facilities Page isn't used")


def edit_facilities(request):
    if request.method == 'POST':
        data = request.POST
        data = data.copy()
        data.pop('csrfmiddlewaretoken', None)
        write_file('facilities.json', data)
        return redirect('SinglePagesApp:facilities')
    else:
        name = 'facilities'
        data = read_file('facilities.json')
        form = EditFacilitiesForm(data)
        return render(request, 'single_pages/edit.html', context={'name': name, 'form': form})


