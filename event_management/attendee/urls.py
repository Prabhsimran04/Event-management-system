from django.urls import path
from . import views

urlpatterns = [
    path("", views.landingPage, name="landingPage"),
    path("register", views.registerPage, name="registerPage"),
    path("api/register", views.register),
    path("api/login", views.login_view),
    path("event", views.eventPage, name="eventPage"),
    path("eventdetail/<str:event_id>", views.eventdetailPage, name="event_detail"),
    path("hostevent", views.hosteventPage, name="hostEvent"),
    path("dashboard", views.dashboardPage, name="hostDashboard"),
    path("viewattendees", views.viewattendeesPage, name="view_attendees"),
    path("dashboard_events", views.dashboard_eventsPage, name="dashboard_events"),
    path("dashboard_user", views.dashboard_userPage, name="dashboard_user"),
]