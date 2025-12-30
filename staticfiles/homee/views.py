from django.shortcuts import render,redirect
from homee.models import *
from django.http import HttpResponse

data = {} 

def home(request):
    description_Data = description.objects.all()
    for desc in description_Data:
        data['title'] = desc.page_title
        data['profile_image'] = desc.profile_photo.url
        data['short_description'] = desc.short_description
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

    project_data = Projects.objects.all()
    data["projects"] = project_data
    
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
 
    return render(request, "portfolio_html.html", data)