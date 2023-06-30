from django.shortcuts import render
import datetime
now=datetime.datetime.now()

# Create your views here.
def index(request):
    return render(request, "LeapYear/LeapYear.html",{
        "leapyear":(now.year%400==0) or (now.year%4==0 and now.year%100!=0)
    })

