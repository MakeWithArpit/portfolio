from django.shortcuts import render,redirect
from homee.models import *
from django.http import HttpResponse

data = {} 

def home(request):
    descriptionData = description.objects.all()
    for desc in descriptionData:
        # Page title
        data['title'] = desc.page_title

        # Profile photo
        data['profile_image'] = desc.profile_photo.url
        
        # Short description for hero section
        data['short_description'] = desc.short_description
        
        # Long description split into paragraphs
        data['para1'] = desc.long_Para1
        data['para2'] = desc.long_Para2
        data['para3'] = desc.long_Para3 

    # Social media and contact links
    email= "arpit.gangwar061@gmail.com"
    github= "MakeWithArpit"
    linkedin= "arpit-gangwar"
    youtube= "arpitgangwar-0.1"
    data['github_url'] = "https://github.com/" + github
    data['linkedin_url'] = "https://www.linkedin.com/in/" + linkedin
    data['youtube_url'] = "https://www.youtube.com/@" + youtube
    data['email'] = "https://mail.google.com/mail/?view=cm&fs=1&to=" + email

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
        {"Degree": "Bachelor of Technology", 
         "Institution": "Invertis University, Bareilly", 
         "Year": "2022 - 2028", 
         "Branch": "Computer Science and Engineering (CSE)"},
    ]

    # Projects list
    data["projects"] = [

        {"project_title": "Renewable Energy Monitoring System",
         "short_description": "An IoT-based solution developed for monitoring solar and wind microgrids in rural areas. The system provides real-time insights into energy generation, storage, and consumption, enabling better decision-making and efficient energy management at the community level.",
         "featured": True,
         "technologies": ["ESP32", 
                          "IoT Sensors", 
                          "Web Dashboard", 
                          "HTML/CSS/JS", 
                          "Cloud Integration"
                          ],  
         "points": [
                "Real-time monitoring of solar and wind energy systems.",
                "Live IoT dashboard for data visualization.",
                "Alerts for inefficiencies and maintenance requirements.",
                "Designed to improve microgrid efficiency by up to 15%."
            ]
        },

        {"project_title": "Smart Air Quality Monitoring System",
         "short_description": "A real-time air quality monitoring system that measures temperature, humidity, CO₂, VOCs, and harmful gases. Sensor data is processed by ESP32 and visualized on a cloud dashboard.",
         "featured": False,
         "technologies": ["ESP32", 
                          "DHT11", 
                          "SGP30", 
                          "MQ Sensors", 
                          "ThingsBoard"
                          ],  
         "points": [
                "Real-time environmental monitoring.",
                "Cloud-based data visualization.",
                "OLED display for local output.",
                "IoT dashboard integration."
            ]
        },

        {"project_title": "Water Tank Level Monitoring & Control",
         "short_description": "An IoT-based system to monitor water tank levels, calculate daily water consumption, and control a water motor both manually and remotely.",
         "featured": False,
         "technologies": ["ESP32", 
                          "Ultrasonic Sensor", 
                          "Relays", 
                          "Google Sheets", 
                          "ThingsBoard"
                          ],  
         "points": [
                "Live tank level & consumption tracking.",
                "Automatic and manual motor control.",
                "Google Sheets integration for data logging.",
                "Cloud monitoring via ThingsBoard."
            ]
        },

        {"project_title": "Student Portfolio Website",
         "short_description": "A personal portfolio website built using Django to showcase skills, projects, and learning journey with dynamic content management.",
         "featured": False,
         "technologies": [ 
                          "Django", 
                          "HTML/CSS/JS", 
                          "Python"
                          ],  
         "points": [
                "Dynamic content management.",
                "Clean UI & responsive design.",
                "Django backend integration.",
                "Project and skill showcase."
            ]
        },

        {"project_title": "Student Portfolio Website",
         "short_description": "A personal portfolio website built using Django to showcase skills, projects, and learning journey with dynamic content management.",
         "featured": False,
         "technologies": [ 
                          "Django", 
                          "HTML/CSS/JS", 
                          "Python"
                          ],  
         "points": [
                "Secure login using file handling.",
                "User-specific task management.",
                "Text-based data storage.",
                "Modular program structure."
            ]
        },
    ]

    # Certifications list
    data["certifications"] = [
        {"cert_title": "Virtual Internship on Industrial Automation",
         "cert_image": "static/Certificate_1.jpg",
         "issued_by": "AICTE-EduSkills",
         "issue_date": "December 2025",
        },
        {"cert_title": "Python for Data Science, AI & Development",
         "cert_image": "static/Certificate_2.jpg",
         "issued_by": "IBM",
         "issue_date": "April 2025",
        },
        {"cert_title": "Crash Course on Python",
         "cert_image": "static/Certificate_3.jpg",
         "issued_by": "Google",
         "issue_date": "February 2025",
        },
        {"cert_title": "Course on Computer Concepts",
         "cert_image": "static/Certificate_4.jpg",
         "issued_by": "NIELIT",
         "issue_date": "December 2020",
        },
    ]

    # Contacet information
    data['contact'] = [
        {"name" :email, "link": data['email'], "icon":"fas fa-envelope"},
        {"name" :"github.com/MakeWithArpit", "link": data['github_url'], "icon": "fab fa-github"},
        {"name" :"linkedin.com/in/arpit-gangwar", "link": data['linkedin_url'], "icon":"fab fa-linkedin"},
        {"name" :"youtube.com/@arpitgangwar-0.1", "link": data['youtube_url'], "icon":"fab fa-youtube"},
    ]

    return render(request, "portfolio_html.html", data)