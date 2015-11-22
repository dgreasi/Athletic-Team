from django.db import models


# Create your models here.
class Team(models.Model):
    pass


class Player(models.Model):
    pass


class Match(models.Model):
    # model fields
    home_pts = models.PositiveSmallIntegerField(blank=True, null=True)
    away_pts = models.PositiveSmallIntegerField(blank=True, null=True)

    stadium = models.CharField(max_length=30, blank=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True,null=True)
    info = models.TextField(blank=True)

    # model relationships
    home_team = models.ForeignKey(Team, related_name='home_team')
    away_team = models.ForeignKey(Team, related_name='away_team')

    players = models.ManyToManyField(Player, through='MatchPlayerStatistics')

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Match._meta.fields]


class MatchPlayerStatistics(models.Model):
    match = models.ForeignKey(Match)
    player = models.ForeignKey(Player)

    started = models.BooleanField()
    time_played = models.CharField(max_length=10, blank=True)
    pts = models.PositiveSmallIntegerField(blank=True, null=True)
    two_pa = models.PositiveSmallIntegerField(blank=True, null=True)
    two_pm = models.PositiveSmallIntegerField(blank=True, null=True)
    three_pa = models.PositiveSmallIntegerField(blank=True, null=True)
    three_pm = models.PositiveSmallIntegerField(blank=True, null=True)
    fta = models.PositiveSmallIntegerField(blank=True, null=True)
    ftm = models.PositiveSmallIntegerField(blank=True, null=True)
    tov = models.PositiveSmallIntegerField(blank=True, null=True)
    oreb = models.PositiveSmallIntegerField(blank=True, null=True)
    dreb = models.PositiveSmallIntegerField(blank=True, null=True)
    ast = models.PositiveSmallIntegerField(blank=True, null=True)
    stl = models.PositiveSmallIntegerField(blank=True, null=True)
    blk = models.PositiveSmallIntegerField(blank=True, null=True)
    pf = models.PositiveSmallIntegerField(blank=True, null=True)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in MatchPlayerStatistics._meta.fields]
