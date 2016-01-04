from django.db import models
from django.contrib.auth.models import User


# Create your models here.
from multiselectfield import MultiSelectField


class Person(models.Model):
    first_name = models.CharField(max_length=30,)
    last_name = models.CharField(max_length=30)
    info = models.TextField()
    image = models.ImageField(upload_to='photos/', blank=True ,default = 'photos/index.png')
    #user = models.ForeignKey(User, default='')

    def __str__(self):              # __unicode__ on Python 2
        return self.last_name


    class Meta:
        abstract = True


class Team(models.Model):
    team_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='photos/', blank=True ,default = 'photos/index.png')
    owned = models.BooleanField()
    
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

    height = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    weight = models.PositiveSmallIntegerField(null=True)
    birth_date = models.DateField(null=True)
    primary_position = models.CharField(max_length=2, choices=available_positions)
    secondary_positions = models.CharField(max_length=30)
    number = models.PositiveSmallIntegerField(null=True)
    overall_rank = models.PositiveSmallIntegerField(blank=True, null=True, default=0)
    nationality = models.CharField(max_length=30)

    # model relationships
    team = models.ForeignKey(Team)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Player._meta.fields]

    def __str__(self):              # __unicode__ on Python 2
        return self.last_name
  
class Match(models.Model):
    # model fields
    home_pts = models.PositiveSmallIntegerField(null=True)
    away_pts = models.PositiveSmallIntegerField(null=True)

    stadium = models.CharField(max_length=30)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    info = models.TextField()

    # model relationships
    home_team = models.ForeignKey(Team, related_name='home_team', null=True)
    away_team = models.ForeignKey(Team, related_name='away_team', null=True)

    home_away = models.CharField(max_length=30)

    players = models.ManyToManyField(Player, through='MatchPlayerStatistics')

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Match._meta.fields]

    def __str__(self):              # __unicode__ on Python 2
        return self.stadium


class MatchPlayerStatistics(models.Model):
    match = models.ForeignKey(Match)
    player = models.ForeignKey(Player)

    started = models.BooleanField()
    time_played = models.CharField(max_length=10)
    pts = models.PositiveSmallIntegerField(null=True)
    two_pa = models.PositiveSmallIntegerField(null=True)
    two_pm = models.PositiveSmallIntegerField(null=True)
    three_pa = models.PositiveSmallIntegerField(null=True)
    three_pm = models.PositiveSmallIntegerField(null=True)
    fta = models.PositiveSmallIntegerField(null=True)
    ftm = models.PositiveSmallIntegerField(null=True)
    tov = models.PositiveSmallIntegerField(null=True)
    oreb = models.PositiveSmallIntegerField(null=True)
    dreb = models.PositiveSmallIntegerField(null=True)
    ast = models.PositiveSmallIntegerField(null=True)
    stl = models.PositiveSmallIntegerField(null=True)
    blk = models.PositiveSmallIntegerField(null=True)
    pf = models.PositiveSmallIntegerField(null=True)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in MatchPlayerStatistics._meta.fields]


class Ranking(models.Model):
    player = models.ForeignKey(Player)

    owner = models.ForeignKey(User, null=True)

    power_arm = models.PositiveSmallIntegerField(blank=True, null=True, default=0)
    power_body = models.PositiveSmallIntegerField(blank=True, null=True, default=0)
    power_legs = models.PositiveSmallIntegerField(blank=True, null=True, default=0)
    speed = models.PositiveSmallIntegerField(blank=True, null=True, default=0)
    team_play = models.PositiveSmallIntegerField(blank=True, null=True, default=0)
    co_op = models.PositiveSmallIntegerField(blank=True, null=True, default=0)
    rate_of_pos = models.PositiveSmallIntegerField(blank=True, null=True, default=0)
    two_shots = models.PositiveSmallIntegerField(blank=True, null=True, default=0)
    three_shots = models.PositiveSmallIntegerField(blank=True, null=True, default=0)
    average_rank = models.PositiveSmallIntegerField(blank=True, null=True, default=0)


    class Meta:
        unique_together = ("player", "owner")


    def ranking_algo(self):
        temp = (self.power_arm + self.power_legs + self.power_body + self.speed + self.team_play + self.co_op + self.rate_of_pos + self.two_shots + self.three_shots)/9

        return temp

    def ranking_algorithm(self):
        #get object player
        fplayer = self.player

        rank_obj = Ranking.objects.filter(player=fplayer)

        k=0
        for temp in rank_obj:
            k += temp.ranking_algo()

        overall = k / rank_obj.count()

        return overall


class TeamPlay(models.Model):
    name = models.CharField(max_length=30, default='')
    data = models.TextField()

    def __str__(self):
        return self.name

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in TeamPlay._meta.fields]


class Exercise(models.Model):
    available_types = (('P', 'Personal'), ('T', 'Team'),)
    available_objectives = (
                                ('SPD', 'Speed'),
                                ('STA', 'Stamina'),
                                ('POW', 'Power'),
                                ('MEN', 'Mentality'),
                                ('SHO', 'Shoot'),
                                ('ATK', 'Attack'),
                                ('DEF', 'Defence'),
                                ('DRI', 'Dribbling'),
                                ('PAS', 'Pass'),
                                ('TMW', 'Teamwork'),
                           )

    name = models.CharField(max_length=30, default='')
    type = models.CharField(max_length=1, choices=available_types, default='P')
    duration = models.SmallIntegerField(default=0)  # time in minutes
    obj = MultiSelectField(choices=available_objectives, blank=True)
    desc = models.TextField()

    def __str__(self):
        return self.name

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in TeamPlay._meta.fields]


class Training(models.Model):
    date = models.DateField()
    start = models.TimeField()
    end = models.TimeField()
    location = models.CharField(max_length=30)

    exercises = models.ManyToManyField("Exercise", blank=True)
    team_plays = models.ManyToManyField("TeamPlay", blank=True)
    team = models.ForeignKey("Team", on_delete=models.CASCADE)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Training._meta.fields]


class Category(models.Model):
    name = models.CharField(max_length=30, default='name')
    season = models.CharField(max_length=30, default='2015-2016')

    def __str__(self):              # __unicode__ on Python 2
        return self.name

    class Meta:
        abstract = True


class League(Category):
    teams = models.ManyToManyField(Team, through='LeagueTeamRel')


class LeagueTeamRel(models.Model):
    gp = models.PositiveSmallIntegerField(default=0)
    wins = models.PositiveSmallIntegerField(default=0)
    loses = models.PositiveSmallIntegerField(default=0)
    pts_difference = models.SmallIntegerField(default=0)
    pts = models.SmallIntegerField(default=0)

    league = models.ForeignKey(League)
    team = models.ForeignKey(Team)

    def __str__(self):
        return self.league.name + ' TO ' + self.team.team_name + ' RELATIONSHIP'


class OrganisationalChart(Person):


    SOM= 'Sports Organizational Manager'
    YDTM= 'Youth Department Techincal Manager'
    YDOM = 'Youth Department Organization Manager'
    SCM = 'Sports Communications Manager'
    TM = 'Team Manager'
    TS = 'Technical Secretariat'
    GOSPM = 'General Operations & Special Projects Manager'
    DSOM = 'Developement & Stadium Operation Manager'
    CM = 'Commercial Manager'
    ICM = 'Institutional Communication Manager'
    FGSD = 'Facilities & General Services Director'
    SM = 'Security Manager'
    SOM = 'Stadium Operation Manager'
    SaSM = 'Sponsorship & Sales Manager'
    # model fields
    available_positions = (
                            (SOM,'Sports Organizational Manager'),
                            (YDTM,'Youth Department Techincal Manager'),
                            (YDOM, 'Youth Department Organization Manager'),
                            (SCM, 'Sports Communications Manager'),
                            (TM, 'Team Manager'),
                            (TS,'Technical Secretariat'),
                            (GOSPM,'General Operations & Special Projects Manager'),
                            (DSOM, 'Developement & Stadium Operation Manager'),
                            (CM, 'Commercial Manager'),
                            (ICM, 'Institutional Communication Manager'),
                            (FGSD,'Facilities & General Services Director'),
                            (SM, 'Security Manager'),
                            (SOM, 'Stadium Operation Manager'),
                            (SaSM,'Sponsorship & Sales Manager'),

                        )
    position = models.CharField(max_length=50, choices=available_positions, blank=True)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in OrganisationalChart._meta.fields]

