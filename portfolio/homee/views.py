from django.shortcuts import render,redirect
from django.http import HttpResponse

data = {} 

def home(request):
    data['title'] = "Arpit Gangwar - Portfolio"
    data['short_description'] = """Tech enthusiast building practical solutions with IoT, Python, and Django. Transforming ideas into real-world applications."""
    data['github_url'] = "https://images.pexels.com/photos/799443/pexels-photo-799443.jpeg"
    data['linkedin_url'] = "https://www.linkedin.com/in/arpit-gangwar"
    data['youtube_url'] = "https://www.youtube.com/@arpitgangwar-0.1"
    data['email'] = "arpit.gangwar061@gmail.com"
    print(data['github_url'])
    return render(request, "portfolio_html.html", data)