from django.contrib import admin
from .models import Event, Participant

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'price', 'organizer')
    search_fields = ('title', 'location', 'organizer')

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'event')
    search_fields = ('full_name', 'email')