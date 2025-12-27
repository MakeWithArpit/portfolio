from django.shortcuts import render,redirect
from homee.models import *
from django.http import HttpResponse

data = {} 

def home(request):
    description_Data = description.objects.all()
    for desc in description_Data:
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

    certificate_data = Certificates.objects.all()
    data['certifications'] = certificate_data

    social_links_data = social_links.objects.all()
    data['social_links'] = social_links_data

    qualifications_data = qualifications.objects.all()
    data["qualifications"] = qualifications_data

    skill_data = skills.objects.all()
    data["skills"] = skill_data
    
    workk = work.objects.get(id=1)
    number_of_projects = int(workk.number_of_projects)
    number_of_certifications = int(workk.number_of_certifications)
    starting_year = int(workk.started_year)

    def format_count(value, ranges):
        for min_val, max_val, label in ranges:
            if min_val <= value <= max_val:
                return label
        return str(value)

    project_ranges = [
        (5, 9, "5+"),
        (10, 14, "10+"),
        (15, 19, "15+"),
        (20, 24, "20+"),
    ]

    cert_ranges = [
        (3, 4, "3+"),
        (5, 7, "5+"),
        (8, 10, "8+"),  
    ]

    data['number_of_projects'] = format_count(number_of_projects, project_ranges)
    data['number_of_certifications'] = format_count(number_of_certifications, cert_ranges)
    data['starting_year'] = str(starting_year)

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


    return render(request, "portfolio_html.html", data)