from django.urls import path
from . import views

app_name = 'importacao'

urlpatterns = [
    path('', views.home, name='home'),
    path('secao/', views.secao_list, name='secao_list'),
    path('cdd/', views.cdd_list, name='cdd_list'),
    path('cdu/', views.cdu_list, name='cdu_list'),
    path('cutter/', views.cutter_list, name='cutter_list'),
    
    # URLs para Livros
    path('livros/', views.livro_list, name='livro_list'),
    path('livros/novo/', views.livro_create, name='livro_create'),
    path('livros/<int:pk>/editar/', views.livro_update, name='livro_update'),
    path('livros/<int:pk>/excluir/', views.livro_delete, name='livro_delete'),
    
    # APIs para busca
    path('api/search/secao/', views.api_search_secao, name='api_search_secao'),
    path('api/search/cdd/', views.api_search_cdd, name='api_search_cdd'),
    path('api/search/cdu/', views.api_search_cdu, name='api_search_cdu'),
    path('api/search/cutter/', views.api_search_cutter, name='api_search_cutter'),
    path('api/gerar-cutter/', views.api_gerar_cutter, name='api_gerar_cutter'),
    
    # Alunos
    path('alunos/', views.aluno_list, name='aluno_list'),
] 