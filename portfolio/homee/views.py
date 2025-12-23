from django.shortcuts import render,redirect
from django.http import HttpResponse

data = {} 

def home(request):
    data['title'] = "Arpit Gangwar - Portfolio"
    data['short_description'] = """Tech enthusiast building practical solutions with IoT, Python, and Django. Transforming ideas into real-world applications."""
    return render(request, "portfolio_html.html", data)