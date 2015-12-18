from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    info = models.TextField(blank=True)
    image = models.ImageField(upload_to='photos/', blank=True)

    class Meta:
        abstract = True


class Team(models.Model):
    team_name = models.CharField(max_length=30, blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.team_name

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Team._meta.fields]


class CoachingStaffMember(Person):
    # model fields
    position = models.CharField(blank=True, max_length=30)

    # model relationships
    team = models.ForeignKey(Team)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in CoachingStaffMember._meta.fields]


class Player(Person):
    # model fields
    PG = 'PG'
    SG = 'SG'
    SF = 'SF'
    PF = 'PF'
    CE = 'CE'
    available_positions = (
                            (PG, 'Point Guard'),
                            (SG, 'Shooting Guard'),
                            (SF, 'Small Forward'),
                            (PF, 'Power Forward'),
                            (CE, 'Center'),
                        )

    height = models.DecimalField(blank=True, max_digits=3, decimal_places=2, null=True)
    weight = models.PositiveSmallIntegerField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    primary_position = models.CharField(max_length=2, choices=available_positions, blank=True)
    secondary_positions = models.CharField(max_length=30, blank=True)
    number = models.PositiveSmallIntegerField(blank=True, null=True)

    nationality = models.CharField(max_length=30, blank=True)

    # model relationships
    team = models.ForeignKey(Team)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Player._meta.fields]


class Match(models.Model):
    # model fields
    home_pts = models.PositiveSmallIntegerField(blank=True, null=True)
    away_pts = models.PositiveSmallIntegerField(blank=True, null=True)

    stadium = models.CharField(max_length=30, blank=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True,null=True)
    info = models.TextField(blank=True)

    # model relationships
    home_team = models.ForeignKey(Team, related_name='home_team',null=True)
    away_team = models.ForeignKey(Team, related_name='away_team',null=True)

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


class TeamPlay(models.Model):
    name = models.CharField(max_length=30, default='')
    data = models.TextField()

    def __str__(self):
        return self.name

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in TeamPlay._meta.fields]
