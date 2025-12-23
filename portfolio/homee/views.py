from django.shortcuts import render,redirect
from django.http import HttpResponse

data = {} 

def home(request):
    data['title'] = "Arpit Gangwar - Portfolio"
    
    data['short_description'] = """Tech enthusiast building practical solutions with IoT, Python, and Django. Transforming ideas into real-world applications."""
    
    data['github_url'] = "https://github.com/MakeWithArpit"
    data['linkedin_url'] = "https://www.linkedin.com/in/arpit-gangwar"
    data['youtube_url'] = "https://www.youtube.com/@arpitgangwar-0.1"
    data['email'] = "arpit.gangwar061@gmail.com"

    data['profile_image'] = "https://i.ibb.co/ymffYc9Q/Photo.jpg"

    return render(request, "portfolio_html.html", data)