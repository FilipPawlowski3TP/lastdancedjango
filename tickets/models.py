from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    CATEGORY_CHOICES = [
        ('computer', 'Komputer'),
        ('printer', 'Drukarka'),
        ('other', 'Inne'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    status = models.CharField(max_length=20, choices=[('pending', 'Oczekujące'), ('in_progress', 'W trakcie'), ('resolved', 'Rozwiązane')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='ticket_images/', null=True, blank=True)  # Upewnij się, że to jest poprawnie
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tickets')

    def __str__(self):
        return self.title

