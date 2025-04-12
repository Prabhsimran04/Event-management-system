from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    name=models.CharField(max_length=50)
    info=models.CharField(max_length=255)
    description=models.TextField()
    venue=models.CharField(max_length=255)
    date=models.DateField()
    grade1_price=models.FloatField()
    grade2_price=models.FloatField()
    grade3_price=models.FloatField()
    url=models.URLField()


class attendee(models.Model):
    userid=models.ForeignKey(to=User,on_delete=models.CASCADE)
    event=models.ManyToManyField(to=Event,related_name="attendees")

class RequestedEvent(models.Model):
    name = models.CharField(max_length=50)
    info = models.CharField(max_length=255)
    venue = models.CharField(max_length=255)
    date = models.DateField()
    grade1_price = models.FloatField()
    grade2_price = models.FloatField()
    grade3_price = models.FloatField()
    description = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.name
    

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=15)  # Use CharField to allow leading zeroes or symbols
    date = models.DateField()

    def __str__(self):
        return f"Appointment for {self.name} on {self.date}"
