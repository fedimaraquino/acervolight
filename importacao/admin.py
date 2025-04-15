from django.contrib import admin
from .models import Secao, CDD, CDU, Cutter, Livro, Aluno

@admin.register(Secao)
class SecaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(CDD)
class CDDAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descricao')
    list_filter = ('codigo',)
    search_fields = ('codigo', 'descricao')

@admin.register(CDU)
class CDUAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descricao')
    list_filter = ('codigo',)
    search_fields = ('codigo', 'descricao')

@admin.register(Cutter)
class CutterAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descricao')
    list_filter = ('codigo',)
    search_fields = ('codigo', 'descricao')

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'ano_publicacao', 'editora', 'secao', 'cdd', 'cdu', 'cutter')
    list_filter = ('secao', 'ano_publicacao')
    search_fields = ('titulo', 'autor', 'editora')
    date_hierarchy = 'data_cadastro'

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'dt_nascimento', 'genero', 'turma', 'serie', 'ano')
    list_filter = ('genero', 'raca', 'turma', 'serie', 'ano', 'cidade', 'uf')
    search_fields = ('nome', 'cpf', 'nome_mae', 'nome_responsavel')
    date_hierarchy = 'dt_nascimento'
    
admin.site.register(Aluno, AlunoAdmin)
