from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.
def f11(request):
    return HttpResponse("<h2 style='color:Blue;'>Hello,Good morning user..!! have a nice day...</h2><hr/>")

