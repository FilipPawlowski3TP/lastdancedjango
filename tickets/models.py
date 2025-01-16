from django.db import models
from django.contrib.auth.models import User


class Ticket(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Oczekujące'),
        ('in_progress', 'W trakcie'),
        ('resolved', 'Rozwiązane'),
    ]

    CATEGORY_CHOICES = [
        ('komputer', 'Komputer'),
        ('drukarka', 'Drukarka'),
        ('inny', 'Inny'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='oczekujące')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='inny')
    image = models.ImageField(upload_to='ticket_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Dodajemy pole updated_at

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
    assigned_to = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL,
                                    related_name='assigned_tickets')

    def __str__(self):
        return self.title

    def get_status_color(self):
        if self.status == 'pending':
            return '#FF0000'
        elif self.status == 'in_progress':
            return '#ffc107'
        elif self.status == 'resolved':
            return '#28a745'
        return '#6c757d'  # Kolor szary jako domyślny
