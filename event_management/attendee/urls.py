from django.urls import path
from . import views

urlpatterns = [
    path("", views.landingPage),
    path("register", views.registerPage),
    path("api/register", views.register),
    path("api/register", views.login_view),
    path("event", views.eventPage),
]