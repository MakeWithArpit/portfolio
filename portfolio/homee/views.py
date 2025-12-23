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
    return render(request, "portfolio_html.html", data)