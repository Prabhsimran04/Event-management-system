from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from .models import *  
from django.shortcuts import redirect


import json

# Create your views here.
def landingPage(request):
    return render(request, 'landingPage.html')


def registerPage(request):
    return render(request, 'register.html')

def eventdetailPage(request, event_id):

    return render(request, 'eventdetail.html')

def hosteventPage(request):
    return render(request, 'hostevent.html')

def dashboardPage(request):
    return render(request, 'dashboard.html')

def viewattendeesPage(request):
    return render(request, 'viewattendees.html')

def dashboard_userPage(request):
    context = {
        "events": []
    }
    events = Event.objects.all()
    for event in events:
        context["events"].append(event)
    return render(request, 'dashboard_user.html', context)


def dashboard_eventsPage(request):
    if not request.user.is_authenticated:
        redirect('')
    context = {
        "events": []
    }
    events = Event.objects.all()
    for event in events:
        context["events"].append(event)
    return render(request, 'dashboard_events.html', context)


@csrf_exempt
def register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('register_username')
            email = data.get('register_email')
            password = data.get('register_password')
            phone_number = data.get('register_phone_number')
            print(data)

            # Create a new user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return JsonResponse({'success': True})

        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Invalid JSON.'})
        except Exception as e:
            print(e)
            return JsonResponse({'success': False, 'message': str(e)})

    return JsonResponse({'success': False, 'message': 'Invalid request method.'})

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        username = data.get('login_username')
        password = data.get('login_password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid credentials.'})

    return JsonResponse({'success': False, 'message': 'Invalid request method.'})

def eventPage(request):
    if request.user.is_authenticated:
        redirect('/dashboard_events')
    context = {
        "events": []
    }
    events = Event.objects.all()
    for event in events:
        context["events"].append(event)
    return render(request, 'event.html',context)