from django.contrib import admin
from .models import Ocorrencia

@admin.register(Ocorrencia)
class OcorrenciaAdmin(admin.ModelAdmin):
    # Isso faz aparecer as colunas bonitinhas no admin
    list_display = ('descricao', 'local', 'status')
    list_filter = ('status', 'local')
    search_fields = ('descricao', 'local')