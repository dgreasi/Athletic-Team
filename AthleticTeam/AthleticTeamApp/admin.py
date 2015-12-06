from django.contrib import admin
from AthleticTeamApp.models import MatchPlayerStatistics, Match, Player, Team, CoachingStaffMember, Ranking


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

class RankingAdmin(admin.ModelAdmin):
	model = Ranking
	extra = 1
	fieldsets = [
		(None, {'fields': ['player', 'owner', 'power', 'speed']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]

	list_display = ('player', 'owner', 'power', 'speed')


admin.site.register(Team, TeamAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Player)
admin.site.register(Ranking, RankingAdmin)
