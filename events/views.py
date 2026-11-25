from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Category, Event, Participant
from .forms import EventForm, ParticipantForm

def home(request):
    events = Event.objects.all().order_by('date')[:3]
    return render(request, 'events/home.html', {
        'events': events,
        'total_events': Event.objects.count(),
        'total_participants': Participant.objects.count(),
    })

def event_list(request):
    query = request.GET.get('q', '')
    category_id = request.GET.get('category', '')
    events = Event.objects.all().order_by('date')
    categories = Category.objects.all()

    if query:
        events = events.filter(
            Q(title__icontains=query) |
            Q(location__icontains=query) |
            Q(organizer__icontains=query)
        )
    if category_id:
        events = events.filter(category_id=category_id)

    return render(request, 'events/events.html', {
        'events': events,
        'categories': categories,
        'query': query,
        'selected_category': category_id,
    })

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event created successfully!')
            return redirect('event_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', {'form': form})

def update_event(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully!')
            return redirect('event_list')
        else:
            messages.error(request, 'Failed to update event. Check the form fields.')
    else:
        form = EventForm(instance=event)
    return render(request, 'events/update_event.html', {'form': form, 'event': event})

def delete_event(request, id):
    event = get_object_or_404(Event, id=id)
    event.delete()
    messages.success(request, 'Event deleted successfully!')
    return redirect('event_list')

def register(request):
    event_id = request.GET.get('event')
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking confirmed! You are successfully registered.')
            return redirect('participants')
        else:
            messages.error(request, 'Registration failed! Please check the error message below.')
    else:
        initial_data = {'event': event_id} if event_id else {}
        form = ParticipantForm(initial=initial_data)
    return render(request, 'events/register.html', {'form': form})

def participants(request):
    all_participants = Participant.objects.select_related('event').all()
    return render(request, 'events/participants.html', {'participants': all_participants})