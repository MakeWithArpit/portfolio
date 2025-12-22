from django.shortcuts import render,redirect
from django.http import HttpResponse

data = {} 

def home(request):
    data['title'] = "Arpit Gangwar - Portfolio"
    return render(request, "portfolio_html.html", data)