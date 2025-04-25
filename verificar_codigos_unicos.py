import os
import django
from typing import Dict, Any
from django.db.models import Model

# Configuração do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblioteca.settings')
django.setup()

from importacao.models import CDD, CDU, Cutter

def contar_codigos_unicos(modelo: Model) -> int:
    """
    Conta o número de códigos únicos em um modelo específico.
    
    Args:
        modelo: Modelo Django para verificar códigos únicos
        
    Returns:
        int: Número de códigos únicos encontrados
    """
    try:
        return modelo.objects.values('codigo').distinct().count()
    except Exception as e:
        print(f"Erro ao contar códigos únicos para {modelo.__name__}: {str(e)}")
        return 0

def verificar_todos_codigos() -> Dict[str, int]:
    """
    Verifica os códigos únicos em todos os modelos.
    
    Returns:
        Dict[str, int]: Dicionário com o nome do modelo e quantidade de códigos únicos
    """
    modelos = {
        'CDD': CDD,
        'CDU': CDU,
        'Cutter': Cutter
    }
    
    resultados = {}
    for nome, modelo in modelos.items():
        resultados[nome] = contar_codigos_unicos(modelo)
    
    return resultados

def exibir_resultados(resultados: Dict[str, int]) -> None:
    """
    Exibe os resultados formatados no console.
    
    Args:
        resultados: Dicionário com os resultados a serem exibidos
    """
    print("\nTOTAL DE CÓDIGOS ÚNICOS:")
    for nome, quantidade in resultados.items():
        print(f"{nome}: {quantidade} códigos únicos")

def main() -> None:
    """
    Função principal que orquestra a execução do script.
    """
    try:
        resultados = verificar_todos_codigos()
        exibir_resultados(resultados)
    except Exception as e:
        print(f"Erro durante a execução: {str(e)}")

if __name__ == "__main__":
    main() 