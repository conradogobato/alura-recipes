from django.contrib import admin
from .models import Pessoa

class Lista_pessoas(admin.ModelAdmin):
    list_display = ['nome', 'email']
    list_display_links = ['nome', 'email']
    search_fields = ['nome']
    list_per_page = 10

admin.site.register(Pessoa, Lista_pessoas)

