from django.contrib import admin
from AthleticTeamApp.models import MatchPlayerStatistics, Match, Player, Team, CoachingStaffMember


# Register your models here.
class CoachingStaffMemberInline(admin.TabularInline):
    model = CoachingStaffMember
    extra = 1


class PlayerInline(admin.TabularInline):
    model = Player
    extra = 1


class TeamAdmin(admin.ModelAdmin):
    inlines = [PlayerInline, CoachingStaffMemberInline]


class MatchPlayerStatisticsInline(admin.TabularInline):
    model = MatchPlayerStatistics
    extra = 1


class MatchAdmin(admin.ModelAdmin):
    inlines = [MatchPlayerStatisticsInline]


admin.site.register(Team, TeamAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Player)
