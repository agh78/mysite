from django.shortcuts import render

from django.http import HttpResponse

def Home_view(request):
    return HttpResponse('<h1>Home page<h1>')  #this is html code

def About_view(request):
    return HttpResponse('<h1>About page<h1>')  #this is html code

def Contact_view(request):
    return HttpResponse('<h1>Contact page<h1>')  #this is html code


