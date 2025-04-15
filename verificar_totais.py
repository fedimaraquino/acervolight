import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblioteca.settings')
django.setup()

from importacao.models import Secao, CDD, CDU, Cutter

print("\nTOTAL DE REGISTROS NO BANCO DE DADOS:")
print(f"Secao: {Secao.objects.count()} registros")
print(f"CDD: {CDD.objects.count()} registros")
print(f"CDU: {CDU.objects.count()} registros")
print(f"Cutter: {Cutter.objects.count()} registros")

print("\nTOTAL DE CÓDIGOS ÚNICOS:")
print(f"CDD: {CDD.objects.values('codigo').distinct().count()} códigos únicos")
print(f"CDU: {CDU.objects.values('codigo').distinct().count()} códigos únicos")
print(f"Cutter: {Cutter.objects.values('codigo').distinct().count()} códigos únicos") 