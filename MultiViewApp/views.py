from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.
def f1(request):
    return HttpResponse("<h2 style='color:blue;'>Good morning user...!! Have a great day</h2><hr/>")

def f2(request):
    return HttpResponse("<h2 style='color:green;'>Good Afternoon user....!! Hope you are doing good...</h2><hr/>")

def f3(request):
    return HttpResponse("<h2 style='color:red;'>Good Evening user...!! How was your day...!!!</h2><hr/>")

