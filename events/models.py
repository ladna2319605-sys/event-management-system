from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='events')
    date = models.DateField()
    location = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    organizer = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.title

class Participant(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='participants')

    def __str__(self):
        return self.full_name