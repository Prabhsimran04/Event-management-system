from django.shortcuts import render

# Create your views here.
def landingPage(request):
    return render(request, 'landingPage.html')


def registerPage(request):
    return render(request, 'register.html')

def eventPage(request):
    context = {
        "events": [
            {
                "title":"Musical Event",
                "details":" A Musical event  by Nirvair Pannu will be held on 30 june 2025 at Guru Nanak Dev University,Amritsar. The event starts at 11.00am to 4.00pm.  ",
            },
            {
                "title":"Book Fair",
                "details":"DAV college,Amritsar held a book fair on 4 july 2025",
            },
            {
                "title":"Carnival",
                "details":" A carnival will be held on june 28 to july 3 2025 at Ranjit Avenue d-block,Amritsar",
            },
        ]
    }
    return render(request, 'event.html',context)

