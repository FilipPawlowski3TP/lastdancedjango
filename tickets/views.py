from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Ticket
from .forms import TicketForm

# Rejestracja użytkownika
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Rejestracja zakończona sukcesem!")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'tickets/register.html', {'form': form})

# Logowanie użytkownika
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Witaj {username}!")
                return redirect('ticket_list')
            else:
                messages.error(request, "Błędna nazwa użytkownika lub hasło.")
        else:
            messages.error(request, "Błędna nazwa użytkownika lub hasło.")
    else:
        form = AuthenticationForm()
    return render(request, 'tickets/login.html', {'form': form})

# Wylogowanie użytkownika
def logout_view(request):
    logout(request)
    messages.info(request, "Zostałeś wylogowany.")
    return redirect('ticket_list')

# Widok dla listy zgłoszeń
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Ticket

# Widok listy zgłoszeń dostępny tylko dla zalogowanych użytkowników
@login_required
def ticket_list(request):
    tickets = Ticket.objects.all().order_by('-created_at')
    return render(request, 'tickets/ticket_list.html', {'tickets': tickets})


# Tworzenie nowego zgłoszenia
def ticket_create(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user  # Przypisanie aktualnie zalogowanego użytkownika
            ticket.save()
            return redirect('ticket_list')
    else:
        form = TicketForm()
    return render(request, 'tickets/ticket_form.html', {'form': form})

from django.shortcuts import render, get_object_or_404
from .models import Ticket

# Widok szczegółów zgłoszenia
def ticket_detail(request, id):
    ticket = get_object_or_404(Ticket, id=id)
    return render(request, 'tickets/ticket_detail.html', {'ticket': ticket})

