from django.shortcuts import render
from django.http import HttpResponse;
import datetime;
# Create your views here.
def f22(request):
    time=datetime.datetime.now();
    print(time)
    msg=("<h2 style 'color=Green;'>Hello user...!!<br /><br /> server date and time::"+str(time)+"</h2><hr/>")
    return HttpResponse(msg);