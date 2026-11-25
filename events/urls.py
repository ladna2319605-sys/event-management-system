# EventHub URL Routing Configuration
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.event_list, name='event_list'),
    path('create/', views.create_event, name='create_event'),
    path('update/<int:id>/', views.update_event, name='update_event'),
    path('delete/<int:id>/', views.delete_event, name='delete_event'),
    path('register/', views.register, name='register'),
    path('participants/', views.participants, name='participants'),
]
