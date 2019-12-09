from django.db import models
from players.models import Player
# Create your models here.

class Guild(models.Model):
    name = models.CharField(max_length=35)
    world_id = models.PositiveIntegerField(default=1)
    ownerid = models.ForeignKey(Player, on_delete=models.PROTECT, db_column='ownerid')
    motd = models.CharField(max_length=50)
    creationdata = models.IntegerField()
    checkdata = models.IntegerField()
    description = models.CharField(max_length=77)
    logo_url = models.CharField(max_length=77)

    class Meta:
        db_table = "guilds"
