from django.contrib import admin
from .models import Curso
# Register your models here.

class CursoAdmin(admin.ModelAdmin):
   
    list_display = (
        'nome', 
        'codigo', 
        'modalidade',
        'carga_horaria',
        'data_inicio',
        'ativo',
    
    )

    search_fields = (
        'nome',
        'codigo'
    )

    list_filter = (
        'modalidade',
        'ativo',
        'data_inicio'
    )

    ordering = (
        'nome',
    )
    list_editable = (
        'ativo',
    )

    readonly_fields = (
        'cadastrado_em',
    )

    list_per_page = 10

    date_hierarchy = 'data_inicio'

    fieldsets = (
        ('Informações do curso', {
            'fields': ('nome', 'codigo', 'descricao')
        }),
        ('Detalhes Acadêmicos', {
            'fields': ('modalidade', 'carga_horaria', 'data_inicio')
        }),
        ('Controle de Cadastro', {
            'fields': ('ativo', 'cadastrado_em')
        })
    )

admin.site.register(Curso, CursoAdmin)
admin.site.site_header = 'Administração Acadêmica'
admin.site.site_title = 'Sistema de Cursos'
admin.site.index_title = 'Gerenciamento de Cursos'