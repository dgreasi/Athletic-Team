from django.contrib import admin

# Register your models here.
from AthleticTeamApp.models import Player, Team


class PlayerInline(admin.TabularInline):
    model = Player
    extra = 1


class TeamAdmin(admin.ModelAdmin):
    inlines = [PlayerInline]


admin.site.register(Team, TeamAdmin)
