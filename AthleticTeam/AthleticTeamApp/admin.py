from django.contrib import admin
from AthleticTeamApp.models import MatchPlayerStatistics, Match, Player, Team


# Register your models here.
class PlayerInline(admin.TabularInline):
    model = Player
    extra = 1


class TeamAdmin(admin.ModelAdmin):
    inlines = [PlayerInline]


class MatchPlayerStatisticsInline(admin.TabularInline):
    model = MatchPlayerStatistics
    extra = 1


class MatchAdmin(admin.ModelAdmin):
    inlines = [MatchPlayerStatisticsInline]


admin.site.register(Team, TeamAdmin)
admin.site.register(Match, MatchAdmin)
