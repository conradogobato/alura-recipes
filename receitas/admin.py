from django.contrib import admin
from .models import receita

class Listando_receitas(admin.ModelAdmin):
    list_display = ['nome_receita', 'publicada']
    search_fields = ['nome_receita']
    list_filter = ["categoria"]
    list_editable = ['publicada']
    list_per_page = 10

admin.site.register(receita, Listando_receitas)