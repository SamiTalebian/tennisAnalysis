from pickle import TRUE
from uuid import uuid4
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django_jalali.db import models as pmodels
import django_jalali.admin as jadmin


class Player(models.Model):
    uuid = models.UUIDField(default=uuid4, null=False, unique=True)
    name = models.CharField(max_length=255, unique=True)
    right_hand = models.BooleanField()
    dob = pmodels.jDateField()
    date_created = pmodels.jDateField(auto_now_add=True)
    height = models.IntegerField(null=True,blank=True)
    weight = models.IntegerField(null=True,blank=True)

    def __str__(self) -> str:
        return self.name

class Payment(models.Model):
    payment_date = pmodels.jDateField(null=True, blank=True)
    staff = models.ForeignKey('Staff', related_name='payments', on_delete=models.DO_NOTHING)
    amount = models.CharField(max_length=255, null=False, blank=True)

    def __str__(self) -> str:
        return str(self.payment_date)


class Staff(models.Model):
    STAFF_CHOICES = [
        ('1', 'Coach'),
        ('2', 'Trainer'),
    ]

    name = models.CharField(max_length=255, unique=True)
    date_created = pmodels.jDateField(auto_now_add=True)
    staff_type = models.CharField(max_length=2 ,choices=STAFF_CHOICES ,default=1)

    def __str__(self) -> str:
        return f'{self.name}'



class TechnicalRecord(models.Model):
    RANGE_VALIDATOR = [MaxValueValidator(100), MinValueValidator(0)]

    forehand = models.IntegerField(validators = RANGE_VALIDATOR,null=True,blank=True,default=0)
    backhand = models.IntegerField(validators = RANGE_VALIDATOR,null=True,blank=True,default=0)
    serve = models.IntegerField(validators = RANGE_VALIDATOR,null=True,blank=True,default=0)
    volley = models.IntegerField(validators = RANGE_VALIDATOR,null=True,blank=True,default=0)
    movement = models.IntegerField(validators = RANGE_VALIDATOR)
    listening = models.IntegerField(validators = RANGE_VALIDATOR)
    class_duration = models.FloatField(default=1, null=False, blank=False)
    date_created = pmodels.jDateField(auto_now_add = True)
    class_date = pmodels.jDateField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    player = models.ForeignKey(Player,related_name='players' ,on_delete=models.DO_NOTHING)
    staff = models.ForeignKey(Staff,related_name="staffs" ,on_delete=models.DO_NOTHING)


class PhysicalRecord(models.Model):
    RANGE_VALIDATOR = [MaxValueValidator(100), MinValueValidator(0)]

    date_created = pmodels.jDateField(auto_now_add = True)
    class_date = pmodels.jDateField(null=True, blank=True)
    stamina = models.IntegerField(validators = RANGE_VALIDATOR)
    stretching = models.IntegerField(validators= RANGE_VALIDATOR)
    movement = models.IntegerField(validators= RANGE_VALIDATOR)
    attention = models.IntegerField(validators= RANGE_VALIDATOR)
    note = models.TextField(null=True, blank=True)
    player = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, blank=True)
    staff = models.ForeignKey(Staff,related_name="staffs_pr" ,on_delete=models.SET_NULL,blank=True, null=True)

class StaffRecord(models.Model):
    RANGE_VALIDATOR = [MaxValueValidator(100), MinValueValidator(0)]

    date_created = pmodels.jDateField(auto_now_add = True)
    class_duration = models.FloatField(default=1, null=False, blank=False)
    mark = models.IntegerField(validators = RANGE_VALIDATOR)
    staff = models.ForeignKey(Staff,related_name="staffs_sr" ,on_delete=models.SET_NULL,blank=True, null=True)


class PlayerMedia(models.Model):
    media_url = models.URLField(max_length=600)
    note = models.TextField()
    date_created = pmodels.jDateField(auto_now_add=True, null=True)
    players = models.ManyToManyField(Player, related_name="player_media")








