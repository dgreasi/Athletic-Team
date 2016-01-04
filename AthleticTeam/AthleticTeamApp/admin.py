from django.contrib import admin

from AthleticTeamApp.models import MatchPlayerStatistics, Match, Player, Team, CoachingStaffMember, Ranking, Exercise, \
    Training, League, LeagueTeamRel, OrganisationalChart


# Register your models here.
class CoachingStaffMemberInline(admin.TabularInline):
    model = CoachingStaffMember
    extra = 1


class PlayerInline(admin.TabularInline):
    model = Player
    extra = 1


class TeamAdmin(admin.ModelAdmin):
    model = Team
    inlines = [PlayerInline, CoachingStaffMemberInline]


class MatchPlayerStatisticsInline(admin.TabularInline):
    model = MatchPlayerStatistics
    extra = 1


class MatchAdmin(admin.ModelAdmin):
    model = Match
    inlines = [MatchPlayerStatisticsInline]


class RankingAdmin(admin.ModelAdmin):
    model = Ranking
    extra = 1
    fieldsets = [
        (None, {'fields': ['player', 'owner', 'power_arm', 'power_body', 'power_legs', 'speed', 'team_play', 'co_op', 'rate_of_pos']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

    list_display = ('player', 'owner', 'power_arm', 'power_body', 'power_legs', 'speed', 'team_play', 'co_op', 'rate_of_pos')


class LeagueTeamRelInline(admin.TabularInline):
    model = LeagueTeamRel
    extra = 1


class LeagueAdmin(admin.ModelAdmin):
    model = League
    inlines = [LeagueTeamRelInline]

class OrganisationalChartInline(admin.TabularInline):
   model = OrganisationalChart
   extra = 1

admin.site.register(Team, TeamAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Training)
admin.site.register(Player)
admin.site.register(Ranking, RankingAdmin)
admin.site.register(Exercise)
admin.site.register(MatchPlayerStatistics)
admin.site.register(League, LeagueAdmin)
admin.site.register(OrganisationalChart)

