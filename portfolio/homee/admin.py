from django.contrib import admin
from django import forms
from django.contrib.admin import register
from homee.models import *

class descriptionAdminForm(forms.ModelForm):
    class Meta:
        model = description
        fields = "__all__"
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

class workAdminForm(forms.ModelForm):
    class Meta:
        model = work
        fields = "__all__"
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

@register(description)
class descriptionAdmin(admin.ModelAdmin):
    form = descriptionAdminForm
    def has_add_permission(self, request): # desable adding more than one entry or delete add button
        if description.objects.exists():
            return False
        return True  
    
    list_display = ('page_title',  'profile_photo', 'short_description', 'long_Para1', 'long_Para2', 'long_Para3' )

@register(work)
class workAdmin(admin.ModelAdmin):
    def has_add_permission(self, request): # desable adding more than one entry or delete add button
        if work.objects.exists():
            return False
        return True  
    form = workAdminForm
    list_display = ('number_of_projects', 'number_of_certifications', 'started_year')

@register(Certificates)
class CertificatesAdmin(admin.ModelAdmin):
    form = CertificatesAdminForm
    list_display = ('cert_title', 'issued_by', 'issue_date', 'cert_image')