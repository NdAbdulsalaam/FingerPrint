from django.contrib import admin
from .models import User, Participant

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'email', 'date_of_birth', 'gender', 'created_at', 'updated_at')
    search_fields = ('username', 'email', 'first_name')

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'created_at', 'updated_at')
    search_fields = ('first_name',)

# Register your models with custom admin configuration
admin.site.register(User, UserAdmin)
admin.site.register(Participant, ParticipantAdmin)