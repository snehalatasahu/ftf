from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.core.validators import MinValueValidator, RegexValidator


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length = 100)
    user = models.OneToOneField(to=User, on_delete=CASCADE)
    image=models.ImageField(upload_to='photos',null=True)
    heartrate=models.CharField(max_length=20)
    dob=models.DateField(auto_now=False, auto_now_add=False)
    weight=models.IntegerField()
    height=models.IntegerField()
    dailygoal=models.IntegerField()
    workouttime=models.IntegerField()
    mon=models.IntegerField()
    tue=models.IntegerField(default=0)
    wed=models.IntegerField()
    thr=models.IntegerField()
    fri=models.IntegerField()
    sat=models.IntegerField()
    sun=models.IntegerField()
    def __str__(self):
        return "%s" % self.user