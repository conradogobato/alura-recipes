from django.contrib import admin
from .models import receita

class Listando_receitas(admin.ModelAdmin):
    list_display = ['nome_receita']
    search_fields = ['nome_receita']
    list_filter = ["categoria"]
    list_per_page = 10

admin.site.register(receita, Listando_receitas)