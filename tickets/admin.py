from django.contrib import admin
from .models import Ticket
from django.utils.html import format_html

class TicketAdmin(admin.ModelAdmin):
    # Zmodyfikuj `list_display`, aby dodać kolumnę z miniaturką obrazu
    list_display = ('title', 'category', 'status', 'user', 'assigned_to', 'created_at', 'updated_at', 'image_preview')
    list_filter = ('status', 'category', 'assigned_to', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
    raw_id_fields = ('user', 'assigned_to')  # Używamy raw_id_fields, żeby wyświetlały się pola wyboru użytkowników

    # Funkcja do wyświetlania miniaturki zdjęcia
    def image_preview(self, obj):
        if obj.image:
            # Formatowanie HTML do wyświetlania miniaturki
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.image.url))
        return "Brak obrazu"
    image_preview.allow_tags = True  # Zezwala na wyświetlanie HTML w tej kolumnie

# Rejestracja modelu Ticket z dostosowanym adminem
admin.site.register(Ticket, TicketAdmin)

