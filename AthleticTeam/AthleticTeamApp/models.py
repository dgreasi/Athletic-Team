from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    info = models.TextField(blank=True)
    #image = models.ImageField(upload_to='photos/', blank=True)

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

class Ranking(models.Model):
    player = models.ForeignKey(Player)

    owner = models.ForeignKey(User, null=True)

    power_arm = models.PositiveSmallIntegerField(blank=True, null=True)
    power_body = models.PositiveSmallIntegerField(blank=True, null=True)
    power_legs = models.PositiveSmallIntegerField(blank=True, null=True)
    speed = models.PositiveSmallIntegerField(blank=True, null=True)
    team_play = models.PositiveSmallIntegerField(blank=True, null=True)
    co_op = models.PositiveSmallIntegerField(blank=True, null=True)
    rate_of_pos = models.PositiveSmallIntegerField(blank=True, null=True)
    two_shots = models.PositiveSmallIntegerField(blank=True, null=True)
    three_shots = models.PositiveSmallIntegerField(blank=True, null=True)


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


# Create your models here.

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