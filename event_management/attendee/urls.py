from django.urls import path
from . import views

urlpatterns = [
    path("", views.landingPage),
    path("register", views.registerPage),
    path("event", views.eventPage),
]