from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from datetime import datetime
from .models import *  
from django.shortcuts import redirect
from django.http import HttpResponse
from collections import defaultdict
from django.utils.timezone import now
from django.utils.safestring import mark_safe


import json

# Create your views here.
def landingPage(request):
    return render(request, 'landingPage.html')


def book_appointment(request):
    if request.method == "POST" and request.headers.get("x-requested-with") == "XMLHttpRequest":
        name = request.POST.get("name")
        email = request.POST.get("email")
        number = request.POST.get("number")
        date = request.POST.get("date")

        Appointment.objects.create(
            name=name,
            email=email,
            number=number,
            date=date
        )
        return JsonResponse({'success': True})

    return JsonResponse({'success': False}, status=400)

def registerPage(request):
    return render(request, 'register.html')

def eventdetailPage(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    user = request.user

    already_booked = False
    booked_grade = -1

    # Only check booking if user is authenticated
    if user.is_authenticated:
        # Check if user has already booked a ticket for this event
        already_booked = TicketBooking.objects.filter(user=user, event=event).exists()

        if already_booked:
            grade = TicketBooking.objects.filter(user=user, event=event).first()
            print(grade.ticket_type)  # optional for debugging
            booked_grade = int(grade.ticket_type[1])  # Assuming ticket_type like 'G1', 'G2', etc.

    # Check if the event date has passed
    event_date_passed = event.date < datetime.now().date()

    return render(request, 'eventdetail.html', {
        'event': event,
        'booked_grade': booked_grade,
        'already_booked': already_booked,
        'event_date_passed': event_date_passed,
    })


@csrf_exempt
def submit_contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        return HttpResponse("OK")  

    return JsonResponse({"error": "Invalid request"}, status=400)
    


    

@csrf_exempt
def eventrequest(request):
    if request.method == 'POST':
        # Extracting the form data from the POST request
        data = json.loads(request.body)
        name = data.get('name')
        info = data.get('info')
        venue = data.get('venue')
        date = data.get('date')
        grade1_price = float(data.get('grade1_price'))
        grade2_price = float(data.get('grade2_price'))
        grade3_price = float(data.get('grade3_price'))
        description = data.get('description')
        url = data.get('url')

        # Create a new RequestedEvent instance and save the data to the database
        requested_event = RequestedEvent(
            name=name,
            info=info,
            venue=venue,
            date=date,
            grade1_price=grade1_price,
            grade2_price=grade2_price,
            grade3_price=grade3_price,
            description=description,
            url=url
        )

        requested_event.save()

        # Optionally, send a success response back to the frontend
        return JsonResponse({'success': True, 'message': 'Event request submitted successfully'})


@login_required
def hosteventPage(request):
    context = {
        "events": []
    }
    events = Event.objects.all()
    for event in events:
        context["events"].append(event.name)
        return render(request, 'hostevent.html', context)
    return render(request, 'hostevent.html')

@login_required
def dashboardPage(request): 
    user = request.user
    bookings = TicketBooking.objects.filter(user=user).select_related('event')
    pie_chart_data = get_spending_share_per_event(user)
    context = {
        'total_events': len(bookings),
        'monthly_bookings': get_monthly_booking_data(user),
        'pie_chart_labels': mark_safe(json.dumps(pie_chart_data['labels'])),
        'pie_chart_data': mark_safe(json.dumps(pie_chart_data)),
        'total_spending': pie_chart_data["total_spending"],
        'connections' : get_all_connections(user),
    }
    print(context)
    return render(request, 'dashboard.html', context)

@login_required
def viewTicketsPage(request):
    user = request.user

    # Get all ticket bookings for the user
    bookings = TicketBooking.objects.filter(user=user).select_related('event')

    # Prepare data for each booking
    tickets = []
    for booking in bookings:
        event = booking.event

        # Determine the ticket price based on ticket_type
        if booking.ticket_type == 'G1':
            ticket_price = event.grade1_price
            ticket_grade = 'Grade 1'
        elif booking.ticket_type == 'G2':
            ticket_price = event.grade2_price
            ticket_grade = 'Grade 2'
        elif booking.ticket_type == 'G3':
            ticket_price = event.grade3_price
            ticket_grade = 'Grade 3'
        else:
            ticket_price = "Unknown"
            ticket_grade = "Unknown"

        tickets.append({
            'ticket_id': booking.id,
            'event_name': event.name,
            'event_date': event.date,
            'ticket_type': ticket_grade,
            'ticket_price': ticket_price,
        })

    context = {
        'tickets': tickets,
        'total_events': len(tickets),
        
    }
    print(context)

    return render(request, 'viewtickets.html', context)


@login_required
def dashboard_userPage(request):
    if not request.user.is_authenticated:
        return redirect('landingPage')
    context = {
        "events": []
    }
    events = Event.objects.all()
    for event in events:
        context["events"].append(event)
    return render(request, 'dashboard_user.html', context)

@login_required
def dashboard_settings(request):
    context = {
        "events": []
    }
    
    return render(request, 'settings.html', context)


@login_required
def dashboard_eventsPage(request):
    user = request.user
    context = {
        "events": []
    }

    events = Event.objects.all()

    for event in events:
        # Try to fetch the ticket booking for this event by the user
        try:
            booking = TicketBooking.objects.get(user=user, event=event)
            event.already_booked = True
            event.ticket_id = booking.id
            event.ticket_type = booking.ticket_type
        except TicketBooking.DoesNotExist:
            event.already_booked = False
            event.ticket_id = None
            event.ticket_type = None

        context["events"].append(event)
    
    print(context)

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
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
       return redirect('/dashboard_events')
    context = {
        "events": []
    }
    events = Event.objects.all()
    for event in events:
        context["events"].append(event)
    return render(request, 'event.html',context)

# Mapping from form ticket type to model choice
TICKET_TYPE_MAP = {
    'standard-access': 'G1',
    'pro-access': 'G2',
    'premium-access': 'G3',
}

@require_POST
@csrf_protect
def book_ticket(request):
    if not request.user.is_authenticated:
        return JsonResponse({'redirect_url': '/register'}, status=401)

    user = request.user
    event_id = request.POST.get('event_id')
    ticket_type_raw = request.POST.get('ticket_type')

    try:
        event = Event.objects.get(id=event_id)
        ticket_type = TICKET_TYPE_MAP.get(ticket_type_raw)
        if not ticket_type:
            return JsonResponse({'error': 'Invalid ticket type'}, status=400)

        booking = TicketBooking.objects.create(
            user=user,
            event=event,
            ticket_type=ticket_type
        )
        return JsonResponse({'message': 'Ticket booked successfully', 'booking_id': booking.id})
    except Event.DoesNotExist:
        return JsonResponse({'error': 'Event not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt  # Remove if you are handling CSRF properly via headers
@login_required
def cancel_booking(request):
    if request.method == "POST":
        user = request.user
        event_id = request.POST.get("event_id")

        try:
            event = Event.objects.get(id=event_id)
            booking = TicketBooking.objects.get(user=user, event=event)
            booking.delete()
            return JsonResponse({"success": True})
        except Event.DoesNotExist:
            return JsonResponse({"success": False, "error": "Event not found."}, status=404)
        except TicketBooking.DoesNotExist:
            return JsonResponse({"success": False, "error": "No booking found."}, status=404)
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=500)

    return JsonResponse({"success": False, "error": "Invalid request method."}, status=405)

def get_monthly_booking_data(user):
    current_year = now().year
    monthly_counts = defaultdict(int)

    bookings = TicketBooking.objects.filter(user=user, booked_on__year=current_year)

    for booking in bookings:
        month = booking.booked_on.month
        monthly_counts[month] += 1

    # Ensure all 12 months are included
    data = [monthly_counts.get(month, 0) for month in range(1, 13)]

    return {
        "labels": ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        "data": data
    }

def get_spending_share_per_event(user):
    bookings = TicketBooking.objects.filter(user=user)
    spending_per_event = defaultdict(float)
    total_spending = 0

    for booking in bookings:
        event = booking.event
        price = 0
        if booking.ticket_type == 'G1':
            price = event.grade1_price
        elif booking.ticket_type == 'G2':
            price = event.grade2_price
        elif booking.ticket_type == 'G3':
            price = event.grade3_price
        
        spending_per_event[event.name] += price
        total_spending += price

    labels = list(spending_per_event.keys())
    data = list(spending_per_event.values())

    return {
        "labels": labels,
        "data": data,
        "total_spending": total_spending
    }



def get_all_connections(user):
    # Step 1: Get all events the user has attended
    user_events = TicketBooking.objects.filter(user=user).values_list('event_id', flat=True)

    # Step 2: Get all users who attended the same events, excluding the current user
    connections = TicketBooking.objects.filter(event_id__in=user_events).exclude(user=user).values_list('user', flat=True).distinct()

    # Step 3: Count unique users
    connection_count = connections.count()

    return connection_count