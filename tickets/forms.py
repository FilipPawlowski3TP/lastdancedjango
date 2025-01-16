from django import forms
from django.contrib.auth.models import User

from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'category', 'image']


from django import forms
from .models import Ticket

class TicketAdminForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'category', 'status', 'image', 'user', 'assigned_to']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['assigned_to'].queryset = User.objects.filter(is_staff=True)  # Tylko użytkownicy będący informatykami
