import os
import pandas as pd
import django

# Configurar o ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblioteca.settings')
django.setup()

# Importar modelos
from importacao.models import Secao, CDD, CDU, Cutter

# Contar registros nas planilhas
print("CONTAGEM DE REGISTROS NAS PLANILHAS:")
secao_count = len(pd.read_excel('secao.xls'))
print(f"secao.xls: {secao_count}")

cdd_count = len(pd.read_excel('CDD.xls'))
print(f"CDD.xls: {cdd_count}")

cdu_count = len(pd.read_excel('CDU.xls'))
print(f"CDU.xls: {cdu_count}")

cutter_count = len(pd.read_excel('Cutter.xls'))
print(f"Cutter.xls: {cutter_count}")

print("\nCONTAGEM DE REGISTROS NO BANCO DE DADOS:")
secao_db_count = Secao.objects.count()
print(f"Tabela Secao: {secao_db_count}")

cdd_db_count = CDD.objects.count()
print(f"Tabela CDD: {cdd_db_count}")

cdu_db_count = CDU.objects.count()
print(f"Tabela CDU: {cdu_db_count}")

cutter_db_count = Cutter.objects.count()
print(f"Tabela Cutter: {cutter_db_count}")

print("\nCOMPARAÇÃO:")
print(f"Secao: {secao_db_count}/{secao_count} ({secao_db_count/secao_count*100:.2f}%)")
print(f"CDD: {cdd_db_count}/{cdd_count} ({cdd_db_count/cdd_count*100:.2f}%)")
print(f"CDU: {cdu_db_count}/{cdu_count} ({cdu_db_count/cdu_count*100:.2f}%)")
print(f"Cutter: {cutter_db_count}/{cutter_count} ({cutter_db_count/cutter_count*100:.2f}%)") 