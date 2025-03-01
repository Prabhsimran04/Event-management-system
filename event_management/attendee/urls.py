from django.urls import path
from . import views

urlpatterns = [
    path("", views.landingPage),
    path("register", views.registerPage),
    path("api/register", views.register),
    path("api/login", views.login_view),
    path("event", views.eventPage),
    path("eventdetail/<str:event_id>", views.eventdetailPage, name="event_detail"),
]