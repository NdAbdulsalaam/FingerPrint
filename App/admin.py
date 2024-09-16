from django.contrib import admin
from .models import Volunteer

class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('first_name',
                    'last_name',
                    'email',
                    'matric_number',
                    'institution',
                    'faculty',
                    'department',
                    'fingerprint'
                    )
    
    search_fields = ('email', 'matric_number')

# Register your models with custom admin configuration
admin.site.register(Volunteer, VolunteerAdmin)