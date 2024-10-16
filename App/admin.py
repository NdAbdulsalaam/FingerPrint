from django.contrib import admin
from .models import Volunteer, Participant

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
    
class ParticipantAdmin(admin.ModelAdmin):
    list_display = (   'id',
                        'image_name'
                    )
    search_fields = ('id', 'image_name')
    sortable_by  = ['image_name']

# Register your models with custom admin configuration
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Participant, ParticipantAdmin)