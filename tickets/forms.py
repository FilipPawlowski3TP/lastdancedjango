from django import forms
from django.contrib.auth.models import User
from .models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'category', 'image']
        labels = {
            'title': 'Tytuł zgłoszenia',
            'description': 'Opis zgłoszenia',
            'category': 'Kategoria',
            'image': 'Załącznik (opcjonalnie)',
        }
        help_texts = {
            'title': 'Podaj krótki tytuł zgłoszenia.',
            'description': 'Opisz szczegóły zgłoszenia.',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Podaj szczegóły zgłoszenia'}),
        }



class TicketAdminForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'category', 'status', 'image', 'user', 'assigned_to']
        labels = {
            'title': 'Tytuł zgłoszenia',
            'description': 'Opis zgłoszenia',
            'category': 'Kategoria',
            'status': 'Status',
            'image': 'Załącznik',
            'user': 'Użytkownik',
            'assigned_to': 'Przypisany informatyk',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['assigned_to'].queryset = User.objects.filter(is_staff=True)  # Tylko użytkownicy będący informatykami



class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Hasło")
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Powtórz hasło")

    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            'username': 'Nazwa użytkownika',
        }

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')

        if password != password_confirm:
            raise forms.ValidationError("Hasła muszą być takie same.")
        return password_confirm
