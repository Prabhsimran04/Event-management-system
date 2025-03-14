from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime


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
    context = {
        "events": [
            {
                "id": 1,
                "title":"Musical Event",
                "info": "Live Concert",
                "price": 350,
                "link": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/4e/75/c8/4e75c88f-2f03-2138-d49f-65cb417bc218/cover.jpg/1200x1200bf-60.jpg",
                "venue": "Guru Nanak Dev University,Amritsar.",
                "description":" A Musical event by Nirvair Pannu and Gurnam  will be held on 30 june 2025 at Guru Nanak Dev University,Amritsar. The event starts at 11.00am to 4.00pm.  ",
                "time": datetime.now().time(),
            },
            {
                "id": 2,
                "title":"Carnival",
                "info": "Fun Fair",
                "price": 200,
                "link": "https://th.bing.com/th/id/OIP.JoVWXx1zBsyHkSMphxbP5gHaE8?rs=1&pid=ImgDetMain",
                "venue": "Kanwar Avenue near Golden Gate,Amritsar.",
                "time": datetime.now().time(),
                "description":" Indian carnivals are vibrant celebrations that showcase the country's rich cultural diversity. They feature colorful parades, traditional music, dance performances, and delicious local cuisine, creating a festive atmosphere that brings communities together. ",
            },
            {
                "id": 3,
                "title":"National Book Fair",
                "info": "Book Fair",
                "price": 0,
                "link": "https://th.bing.com/th/id/OIP.p4v84v-Mbgsf7uHd2mq1cQAAAA?rs=1&pid=ImgDetMain",
                "venue": "DAV College,Amritsar.",
                "time": datetime.now().time(),
                "description":"A book fair is a vibrant event where authors, readers, and booksellers come together to celebrate literature. These gatherings often feature a variety of books, cultural activities, and opportunities for networking, making them enjoyable and enriching experiences for all involved.",
            },
            
        ]
    }
    return render(request, 'event.html',context)