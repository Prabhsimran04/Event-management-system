from django.shortcuts import render

# Create your views here.
def landingPage(request):
    return render(request, 'landingPage.html')


def registerPage(request):
    return render(request, 'register.html')

def eventPage(request):
    return render(request, 'event.html')

