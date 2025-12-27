from django.contrib import admin
from django.contrib.admin import register
from homee.models import *

@register(description)
class descriptionAdmin(admin.ModelAdmin):
    def has_add_permission(self, request): # desable adding more than one entry or delete add button
        if description.objects.exists():
            return False
        return True  
    list_display = ('page_title', 
                    'profile_photo',
                    'short_description',
                    'long_Para1',
                    'long_Para2',
                    'long_Para3'
                    )

# admin.site.register(description, descriptionAdmin)
# Register your models here.
