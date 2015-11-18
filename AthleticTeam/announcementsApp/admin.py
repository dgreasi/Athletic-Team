from django.contrib import admin

# Register your models here.
from .models import Announcement, Comment

#display comments
class CommentInline(admin.TabularInline):
    #number of comments to display
    model = Comment
    extra = 3

class AnnouncementAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['announcement_title', 'announcement_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    #display comments in line
    inlines = [CommentInline]
    #display order
    list_display = ('announcement_title', 'announcement_text', 'pub_date', 'was_published_recently')
    #filter for date publication
    list_filter = ['pub_date']
    #search field
    search_fields = ['announcement_title']

#connect admin/html with announcement
admin.site.register(Announcement, AnnouncementAdmin)
#add comments to display
admin.site.register(Comment)
