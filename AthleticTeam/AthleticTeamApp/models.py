from django.db import models


# Create your models here.
class Team(models.Model):
    pass


class Player(models.Model):
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

    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    height = models.DecimalField(blank=True, max_digits=3, decimal_places=2, null=True)
    weight = models.PositiveSmallIntegerField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    primary_position = models.CharField(max_length=2, choices=available_positions, blank=True)
    secondary_positions = models.CharField(max_length=30, blank=True)
    number = models.PositiveSmallIntegerField(blank=True, null=True)
    info = models.TextField(blank=True)
    nationality = models.CharField(max_length=30, blank=True)
    # image = models.ImageField()

    # model relationships
    team = models.ForeignKey(Team)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Player._meta.fields]
