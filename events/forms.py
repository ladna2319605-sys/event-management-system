from django import forms
from .models import Event, Participant

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'category', 'date', 'location', 'price', 'organizer', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['full_name', 'email', 'phone', 'event']

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        event = cleaned_data.get('event')

        if email and event:
            if Participant.objects.filter(email=email, event=event).exists():
                raise forms.ValidationError("This email is already registered for this event!")
        return cleaned_data