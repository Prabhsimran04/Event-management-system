from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    name=models.CharField(max_length= 50)
    description=models.TextField()
    date=models.DateField()
    grade1_price=models.FloatField()
    grade2_price=models.FloatField()
    grade3_price=models.FloatField()
    url=models.URLField()

class attendee(models.Model):
    userid=models.ForeignKey(to=User,on_delete=models.CASCADE)
    event=models.ManyToManyField(to=Event,related_name="attendees")