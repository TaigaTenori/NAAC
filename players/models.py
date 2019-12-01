from django.db import models

from users.models import Account
# Create your models here.
import time
from naac.functions import get_exp_for_level
from naac import naac_settings as config


class Player(models.Model):
    name = models.CharField(max_length=35)
    world_id = models.PositiveIntegerField(default=1)
    group_id = models.IntegerField(default=1)
    account = models.ForeignKey(Account, models.DO_NOTHING)
    level = models.IntegerField(default=config.starting_level)
    vocation = models.IntegerField()
    health = models.IntegerField(default=150)
    healthmax = models.IntegerField(default=150)
    experience = models.BigIntegerField(default=get_exp_for_level(config.starting_level))
    lookbody = models.IntegerField(default=1)
    lookfeet = models.IntegerField(default=1)
    lookhead = models.IntegerField(default=1)
    looklegs = models.IntegerField(default=1)
    looktype = models.IntegerField(default=1)
    lookaddons = models.IntegerField(default=1)
    maglevel = models.IntegerField(default=1)
    mana = models.IntegerField(default=30)
    manamax = models.IntegerField(default=30)
    manaspent = models.IntegerField(default=0)
    soul = models.PositiveIntegerField(default=100)
    town_id = models.IntegerField(default=1)
    posx = models.IntegerField(default=650)
    posy = models.IntegerField(default=650)
    posz = models.IntegerField(default=7)
    conditions = models.TextField()
    cap = models.IntegerField(default=100)
    sex = models.IntegerField(default=1)
    lastlogin = models.BigIntegerField(default=0)
    lastip = models.PositiveIntegerField(default=1)
    save_character = models.IntegerField(default=1, db_column="save") # was conflicting with model.save()
    skull = models.PositiveIntegerField(default=1)
    skulltime = models.IntegerField(default=0)
    rank_id = models.IntegerField(default=0)
    guildnick = models.CharField(max_length=255)
    lastlogout = models.BigIntegerField(default=1)
    blessings = models.IntegerField(default=1)
    balance = models.BigIntegerField(default=0)
    stamina = models.BigIntegerField(default=42*60*1000)
    direction = models.IntegerField(default=1)
    loss_experience = models.IntegerField(default=1)
    loss_mana = models.IntegerField(default=1)
    loss_skills = models.IntegerField(default=1)
    loss_containers = models.IntegerField(default=1)
    loss_items = models.IntegerField(default=1)
    premend = models.IntegerField(default=0)
    online = models.IntegerField(default=0)
    marriage = models.PositiveIntegerField(default=1)
    promotion = models.IntegerField(default=0)
    deleted = models.IntegerField(default=0)
    description = models.CharField(max_length=77)
    created = models.IntegerField(default=time.time) # the function without () will be called on runtime
    hidden = models.IntegerField(default=0)
    comment = models.TextField()
    exphist_lastexp = models.BigIntegerField(default=1)
    exphist1 = models.BigIntegerField(default=1)
    exphist2 = models.BigIntegerField(default=1)
    exphist3 = models.BigIntegerField(default=1)
    exphist4 = models.BigIntegerField(default=1)
    exphist5 = models.BigIntegerField(default=1)
    exphist6 = models.BigIntegerField(default=1)
    exphist7 = models.BigIntegerField(default=1)
    onlinetimetoday = models.BigIntegerField(default=1)
    onlinetime1 = models.BigIntegerField(default=1)
    onlinetime2 = models.BigIntegerField(default=1)
    onlinetime3 = models.BigIntegerField(default=1)
    onlinetime4 = models.BigIntegerField(default=1)
    onlinetime5 = models.BigIntegerField(default=1)
    onlinetime6 = models.BigIntegerField(default=1)
    onlinetime7 = models.BigIntegerField(default=1)
    onlinetimeall = models.BigIntegerField(default=1)

    def save(self, *args, **kwargs):
        # set starting positions depending on the choice of town
        town = config.temple_position[self.town_id]
        self.posx = town[0] # x
        self.posy = town[1] # y
        self.posz = town[2] # z
        super(Player, self).save(*args, **kwargs)

    class Meta:
        managed = True
        db_table = 'players'
        unique_together = (('name', 'deleted'),)
