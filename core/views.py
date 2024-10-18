from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

#creating the functionm for index 

def index(request):
    return HttpResponse('<h1>Welcome to SocialCube</h1>')
    