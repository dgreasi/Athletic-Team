from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import Comment, Announcement

class FullView(generic.ListView):
    template_name = 'announcementsApp/index.html'
    #For DetailView the Announcement variable is provided automatically 
    #since we are using a Django model (Announcement), Django is able to 
    #determine an appropriate name for the context variable. However, 
    #for ListView, the automatically generated context variable 
    #is Announcement_list. To override this we provide the context_object_name attribute,
    # specifying that we want to use latest_Announcement_list instead
    context_object_name = 'latest_Announcement_list'

    def get_queryset(self):
        """
        Return the last five published Announcements (not including those set to be
        published in the future).
        """
        #showing all announcements
        return Announcement.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')


class IndexView(generic.ListView):
    template_name = 'announcementsApp/index.html'
    #For DetailView the Announcement variable is provided automatically 
    #since we are using a Django model (Announcement), Django is able to 
    #determine an appropriate name for the context variable. However, 
    #for ListView, the automatically generated context variable 
    #is Announcement_list. To override this we provide the context_object_name attribute,
    # specifying that we want to use latest_Announcement_list instead
    context_object_name = 'latest_Announcement_list'

    def get_queryset(self):
        """
        Return the last five published Announcements (not including those set to be
        published in the future).
        """
        #showing 3 recent announcements
        return Announcement.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:3]


class DetailView(generic.DetailView):
    model = Announcement
    template_name = 'announcementsApp/detail.html'
    def get_queryset(self):
        """
        Excludes any Announcements that aren't published yet.
        """
        return Announcement.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Announcement
    template_name = 'announcementsApp/results.html'

def vote(request, announcement_id):
    p = get_object_or_404(Announcement, pk=announcement_id)
    try:
        selected_comment = p.comment_set.get(pk=request.POST['comment'])
    except (KeyError, Comment.DoesNotExist):
        # Redisplay the Announcement voting form.
        return render(request, 'announcementsApp/detail.html', {
            'announcement': p,
            'error_message': "You didn't select a Comment.",
        })
    else:
        selected_comment.votes += 1
        selected_comment.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('announcementsApp:results', args=(p.id,)))
