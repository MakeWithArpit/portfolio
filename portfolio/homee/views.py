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

    # Long description split into paragraphs
    data['para1'] = "Hello! I'm Arpit Gangwar, a tech enthusiast and student who loves learning by building. I have hands-on experience in C, Python, Django, and IoT projects using ESP32 and ESP8266 microcontrollers."
    data['para2'] = "My focus is on creating practical, real-life solutions like automation systems, monitoring dashboards, and web-based tools. I believe in the power of technology to solve everyday problems and improve lives."
    data['para3'] = "Currently pursuing B.Tech in Computer Science and Engineering at Invertis University, I'm working on improving my backend development skills with Django and exploring how hardware and software can work together to solve real problems."

    return render(request, "portfolio_html.html", data)