from django.shortcuts import render,redirect
from django.http import HttpResponse

data = {} 

def home(request):
    return render(request, "portfolio_html.html")