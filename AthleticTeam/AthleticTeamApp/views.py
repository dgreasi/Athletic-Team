from django.shortcuts import render, render_to_response, redirect,get_object_or_404
from django.views import generic

from AthleticTeamApp.forms import ContactForm

from AthleticTeamApp.models import Player, Match, CoachingStaffMember, Team, Ranking, OrganisationalChart
#, OrganisationalChart

from django.http import *
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy

from django.views.generic.detail import SingleObjectMixin
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator

from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context


# Create your views here.

class ShowCoachingStaffMembers(generic.ListView):
    model = CoachingStaffMember
    template_name = 'coaching_staff_member/showall.html'
    context_object_name = 'coachingstaffmember_list'


class ShowCoachingStaffMember(generic.DetailView):
    model = CoachingStaffMember
    template_name = 'coaching_staff_member/show.html'


class ShowPlayers(generic.ListView):
    model = Player
    template_name = 'player/showall.html'
    context_object_name = 'players_list'

class ShowPlayer(generic.DetailView):
    model = Player
    template_name = 'player/show.html'


class ShowMatches(generic.ListView):
    model = Match
    template_name = 'match/showall.html'
    context_object_name = 'matches_list'

class ShowMatch(generic.DetailView):
    model = Match
    template_name = 'match/show.html'


# Create your views here.
class ShowTeams(generic.ListView):
    model = Team
    template_name = 'team/showall.html'
    context_object_name = 'team_players_list'

class ShowTeam(generic.DetailView):
    model = Team
    template_name = 'team/show.html'

def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('home/contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage( "New contact form submission", content, "Your website" +'<hi@teamapp.com>', ['anikola@uth.gr'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return HttpResponseRedirect(reverse('AthleticTeamApp:home'))

    return render(request, 'home/contact.html', {'form': form_class, })


class ShowOrganisationalCharts(generic.ListView):
    model = OrganisationalChart
    template_name = 'organisational_chart/showall.html'
    context_object_name = 'organisational_chart_list'


class ShowOrganisationalChart(generic.DetailView):
    model = OrganisationalChart
    template_name = 'organisational_chart/show.html'
