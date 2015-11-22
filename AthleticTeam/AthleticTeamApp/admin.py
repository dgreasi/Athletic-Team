from django.contrib import admin
from AthleticTeamApp.models import MatchPlayerStatistics, Match


# Register your models here.
class MatchPlayerStatisticsInline(admin.TabularInline):
    model = MatchPlayerStatistics
    extra = 1


class MatchAdmin(admin.ModelAdmin):
    inlines = [MatchPlayerStatisticsInline]


admin.site.register(Match, MatchAdmin)