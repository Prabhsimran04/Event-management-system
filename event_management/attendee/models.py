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

class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    email = models.EmailField(verbose_name="Email")
    subject = models.CharField(max_length=200, verbose_name="Subject")
    message = models.TextField(verbose_name="Message")
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
    
class TicketBooking(models.Model):
    TICKET_TYPE_CHOICES = [
        ('G1', 'Grade 1'),
        ('G2', 'Grade 2'),
        ('G3', 'Grade 3'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    booked_on = models.DateTimeField(auto_now_add=True)
    ticket_type = models.CharField(max_length=10, choices=TICKET_TYPE_CHOICES)

    def __str__(self):
        return f"Ticket for {self.event.name} by {self.user.username}"