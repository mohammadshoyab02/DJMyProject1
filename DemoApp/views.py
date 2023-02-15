from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show(request):
    ss='''
    <h1>welcome to django first project demo app in pycharm</h1><hr/>
    '''
    return HttpResponse(ss);

