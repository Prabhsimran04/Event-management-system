from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("", views.landingPage, name="landingPage"),
    path("register", views.registerPage, name="registerPage"),
    path("api/register", views.register),
    path("api/login", views.login_view),
    path("event", views.eventPage, name="eventPage"),
    path("eventdetail/<str:event_id>", views.eventdetailPage, name="event_detail"),
    path("hostevent", views.hosteventPage, name="hostEvent"),
    path("api/eventrequest", views.eventrequest, name="eventrequest"),
    path("dashboard", views.dashboardPage, name="hostDashboard"),
    # path("viewattendees", views.viewattendeesPage, name="view_attendees"),
    path("dashboard_events", views.dashboard_eventsPage, name="dashboard_events"),
    # path("dashboard_user", views.dashboard_userPage, name="dashboard_user"),
    path('book-appointment/', views.book_appointment, name='book_appointment'),
    path("submit-contact", views.submit_contact, name="submit_contact"),
    path("book-ticket", views.book_ticket, name="book_ticket"),
    path('cancel-booking/', views.cancel_booking, name='cancel_booking'),
    path('view-tickets/', views.viewTicketsPage, name='view_tickets'),
    path('settings/', views.dashboard_settings, name='settings'),
    path('logout/', LogoutView.as_view(next_page='landingPage'), name='logout'),
]