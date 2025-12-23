from django.shortcuts import render,redirect
from django.http import HttpResponse

data = {} 

def home(request):
    # Page title
    data['title'] = "Arpit Gangwar - Portfolio"
    
    # Short description for hero section
    data['short_description'] = """Tech enthusiast building practical solutions with IoT, Python, and Django. Transforming ideas into real-world applications."""
    
    # Social media and contact links
    data['github_url'] = "https://github.com/MakeWithArpit"
    data['linkedin_url'] = "https://www.linkedin.com/in/arpit-gangwar"
    data['youtube_url'] = "https://www.youtube.com/@arpitgangwar-0.1"
    data['email'] = "arpit.gangwar061@gmail.com"

    data['profile_image'] = "https://i.ibb.co/ymffYc9Q/Photo.jpg"

    # Long description split into paragraphs
    data['para1'] = "Hello! I'm Arpit Gangwar, a tech enthusiast and student who loves learning by building. I have hands-on experience in C, Python, Django, and IoT projects using ESP32 and ESP8266 microcontrollers."
    data['para2'] = "My focus is on creating practical, real-life solutions like automation systems, monitoring dashboards, and web-based tools. I believe in the power of technology to solve everyday problems and improve lives."
    data['para3'] = "Currently pursuing B.Tech in Computer Science and Engineering at Invertis University, I'm working on improving my backend development skills with Django and exploring how hardware and software can work together to solve real problems."

    # Number of projects, Certifications, and started years
    number_of_projects = 5
    number_of_certifications = 3
    starting_year = 2024

    if number_of_projects >= 5 and number_of_certifications <= 9:
        data['number_of_projects'] = "5+"
    elif number_of_projects >= 10 and number_of_certifications <= 14:
        data['number_of_projects'] = "10+"
    elif number_of_projects >= 15 and number_of_certifications <= 19:
        data['number_of_projects'] = "15+"
    elif number_of_projects >= 20 and number_of_certifications <= 24:
        data['number_of_projects'] = "20+"
    else:
        data['number_of_projects'] = str(number_of_projects)

    if number_of_certifications >= 3 and number_of_certifications <= 4:
        data['number_of_certifications'] = "3+"
    elif number_of_certifications >= 5 and number_of_certifications <= 7:
        data['number_of_certifications'] = "5+"
    elif number_of_certifications >= 8 and number_of_certifications <= 10:
        data['number_of_certifications'] = "8+"
    else:
        data['number_of_certifications'] = str(number_of_certifications)

    data['starting_year'] = str(starting_year)

    # Skills list

    data["skills"] = [
        {"name": "Python", "icon": "fab fa-python"},
        {"name": "C Language", "icon": "fas fa-code"},
        {"name": "Django", "icon": "fas fa-server"},
        {"name": "ESP32/ESP8266", "icon": "fas fa-microchip"},
        {"name": "HTML/CSS", "icon": "fab fa-html5"},
        {"name": "JavaScript", "icon": "fab fa-js"},
        {"name": "IoT Systems", "icon": "fas fa-network-wired"},
        {"name": "Data Analysis", "icon": "fas fa-database"},
        {"name": "Git/GitHub", "icon": "fab fa-git-alt"}
    ]

    # Academic qualifications
    data["qualifications"] = [
        {"Degree": "Bachelor of Technology", "Institution": "Invertis University, Bareilly", "Year": "2022 - 2028", "Branch": "Computer Science and Engineering (CSE)"},
    ]
    return render(request, "portfolio_html.html", data)