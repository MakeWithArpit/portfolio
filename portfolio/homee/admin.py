from django.contrib import admin
from django import forms
from django.contrib.admin import register
from homee.models import *

class ProjectsAdminForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = "__all__"
        labels = {
            'project_title': 'Project Title',
            'short_description': 'Short Description',
            'featured': 'Featured Project',
            'technologies': 'Technologies Used',
            'points': 'Key Points',
        }
        widgets = {
            'project_title': forms.TextInput(attrs={
                'placeholder': 'Enter project title'
            }),
            'short_description': forms.Textarea(attrs={
                'placeholder': 'Enter short project description',
            }),
            'technologies': forms.Textarea(attrs={
                'placeholder': 'e.g. Django, Python, MySQL',
            }),
            'points': forms.Textarea(attrs={
                'placeholder': 'e.g. Login system, REST API, Admin panel',
            }),
        }

class descriptionAdminForm(forms.ModelForm):
    class Meta:
        model = description
        fields = "__all__"
        labels = {
            'page_title': 'Page Title',
            'short_description': 'Short Description',
            'long_Para1': 'Long Description Paragraph 1',
            'long_Para2': 'Long Description Paragraph 2',
            'long_Para3': 'Long Description Paragraph 3',
        }
        widgets = {
            'page_title': forms.TextInput(attrs={
                'placeholder': 'Enter page title'
            }),
            
            'short_description': forms.Textarea(attrs={
                'placeholder': 'Enter a brief description (max 130 characters)'
            }),

            'long_Para1': forms.Textarea(attrs={
                'placeholder': 'Enter the first paragraph of your long description (max 250 characters)'
            }),

            'long_Para2': forms.Textarea(attrs={
                'placeholder': 'Enter the second paragraph of your long description (max 250 characters)'
            }),

            'long_Para3': forms.Textarea(attrs={
                'placeholder': 'Enter the third paragraph of your long description (max 250 characters)'
            }),
        }

class CertificatesAdminForm(forms.ModelForm):
    class Meta:
        model = Certificates
        fields = "__all__"
        labels = {
            'cert_title': 'Certificate Title',
            'issued_by': 'Issued By',
            'issue_date': 'Issue Date',
        }
        widgets = {
            'cert_title': forms.TextInput(attrs={
                'placeholder': 'Enter certificate title'
            }),
            'issued_by': forms.TextInput(attrs={
                'placeholder': 'Enter the name of the issuing organization'
            }),
            'issue_date': forms.TextInput(attrs={
                'placeholder': 'Enter the issue date (e.g., April 2025)'
            }),
        }

class social_linksAdminForm(forms.ModelForm):
    class Meta:
        model = social_links
        fields = "__all__"
        labels = {
            'platform_name': 'Platform Name',
            'link': 'Profile Link',
            'link_with_username': 'Link with Username',
            'icon_class': 'Icon CSS Class',
        }
        widgets = {
            'platform_name': forms.TextInput(attrs={
                'placeholder': 'Enter the name of the social media platform (e.g., GitHub)'
            }),
            'link': forms.URLInput(attrs={
                'placeholder': 'Enter the full URL to your profile.'
            }),
            'link_with_username': forms.TextInput(attrs={
                'placeholder': 'Enter the link with your username (e.g., github.com/MakeWithArpit)'
            }),
            'icon_class': forms.TextInput(attrs={
                'placeholder': 'Enter the CSS class for the platform icon (e.g., fab fa-github)'
            }),
        }

class workAdminForm(forms.ModelForm):
    class Meta:
        model = work
        fields = "__all__"
        labels = {
            'number_of_projects': 'Number of Projects',
            'number_of_certifications': 'Number of Certifications',
            'started_year': 'Started Year',
        }
        widgets = {
            'number_of_projects': forms.NumberInput(attrs={
                'placeholder': 'Enter total number of projects'
            }),
            'number_of_certifications': forms.NumberInput(attrs={
                'placeholder': 'Enter total number of certifications'
            }),
            'started_year': forms.NumberInput(attrs={
                'placeholder': 'Enter the year you started'
            })
        }

class qualificationsAdminForm(forms.ModelForm):
    class Meta:
        model = qualifications
        fields = "__all__"
        labels = {
            'degree': 'Degree',
            'institution': 'Institution',
            'year': 'Year of Completion',
            'branch': 'Branch / Field of Study',
        }
        widgets = {
            'degree': forms.TextInput(attrs={
                'placeholder': 'Enter degree name'
            }),
            'institution': forms.TextInput(attrs={
                'placeholder': 'Enter institution name'
            }),
            'year': forms.TextInput(attrs={
                'placeholder': 'Enter year of completion'
            }),
            'branch': forms.TextInput(attrs={
                'placeholder': 'Enter branch/field of study'
            }),
        }

class skillsAdminForm(forms.ModelForm):
    class Meta:
        model = skills
        fields = "__all__"
        labels = {
            'skill_name': 'Skill Name',
            'icon_class': 'Icon CSS Class',
        }
        widgets = {
            'skill_name': forms.TextInput(attrs={
                'placeholder': 'Enter skill name'
            }),
            'icon_class': forms.TextInput(attrs={
                'placeholder': 'Enter the CSS class for the skill icon (e.g., fab fa-python)'
            }),
        }

@register(description)
class descriptionAdmin(admin.ModelAdmin):
    form = descriptionAdminForm
    def has_add_permission(self, request): # desable adding more than one entry or delete add button
        if description.objects.exists():
            return False
        return True  
    
    list_display = ('page_title',  'profile_photo', 'short_description', 'long_Para1', 'long_Para2', 'long_Para3' )

@register(social_links)
class social_linksAdmin(admin.ModelAdmin):
    form = social_linksAdminForm
    list_display = ('platform_name', 'link', 'link_with_username', 'icon_class')

@register(work)
class workAdmin(admin.ModelAdmin):
    def has_add_permission(self, request): # desable adding more than one entry or delete add button
        if work.objects.exists():
            return False
        return True  
    form = workAdminForm
    list_display = ('number_of_projects', 'number_of_certifications', 'started_year')

@register(qualifications)
class qualificationsAdmin(admin.ModelAdmin):
    form = qualificationsAdminForm
    list_display = ('degree', 'institution', 'year', 'branch') 

@register(skills)
class skillsAdmin(admin.ModelAdmin):
    form = skillsAdminForm
    list_display = ('skill_name', 'icon_class')

@register(Certificates)
class CertificatesAdmin(admin.ModelAdmin):
    form = CertificatesAdminForm
    list_display = ('cert_title', 'issued_by', 'issue_date', 'cert_image')

@register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    form = ProjectsAdminForm
    list_display = ('project_title',)
