from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def display(request):
    ss='''
    <h1>welcome to django first project first app in pycharm</h1>
    '''
    return HttpResponse(ss);
