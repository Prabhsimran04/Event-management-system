from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Event)
admin.site.register(attendee)
admin.site.register(RequestedEvent)
admin.site.register(Appointment)
admin.site.register(ContactMessage)
admin.site.register(TicketBooking)