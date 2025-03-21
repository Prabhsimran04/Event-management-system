from django.urls import path
from . import views

urlpatterns = [
    path("", views.landingPage),
    path("register", views.registerPage),
    path("api/register", views.register),
    path("api/login", views.login_view),
    path("event", views.eventPage),
    path("eventdetail/<str:event_id>", views.eventdetailPage, name="event_detail"),
    path("hostevent", views.hosteventPage),
    path("dashboard", views.dashboardPage),
    path("viewattendees", views.viewattendeesPage, name="view_attendees"),
    path("dashboard_events", views.dashboard_eventsPage, name="dashboard_events"),
    path("dashboard_user", views.dashboard_userPage, name="dashboard_user"),
]