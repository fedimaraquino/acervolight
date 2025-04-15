import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblioteca.settings')
django.setup()

from importacao.models import CDD, CDU, Cutter

# Verificar quantos códigos únicos existem em cada tabela
print("\nTOTAL DE CÓDIGOS ÚNICOS:")
print(f"CDD: {CDD.objects.values('codigo').distinct().count()} códigos únicos")
print(f"CDU: {CDU.objects.values('codigo').distinct().count()} códigos únicos")
print(f"Cutter: {Cutter.objects.values('codigo').distinct().count()} códigos únicos") 