import pandas as pd

# Verificar duplicatas nas planilhas
print("VERIFICAÇÃO DE CÓDIGOS DUPLICADOS:")

# CDD
df_cdd = pd.read_excel('CDD.xls')
duplicados_cdd = df_cdd[df_cdd.duplicated(subset=['codigo'], keep=False)]
print(f"\nCDD.xls - {len(duplicados_cdd)} códigos duplicados:")
if not duplicados_cdd.empty:
    print(duplicados_cdd.head(10))  # Mostrar primeiros 10 duplicados

# CDU
df_cdu = pd.read_excel('CDU.xls')
duplicados_cdu = df_cdu[df_cdu.duplicated(subset=['codigo'], keep=False)]
print(f"\nCDU.xls - {len(duplicados_cdu)} códigos duplicados:")
if not duplicados_cdu.empty:
    print(duplicados_cdu.head(10))  # Mostrar primeiros 10 duplicados

# Cutter
df_cutter = pd.read_excel('Cutter.xls')
duplicados_cutter = df_cutter[df_cutter.duplicated(subset=['codigo'], keep=False)]
print(f"\nCutter.xls - {len(duplicados_cutter)} códigos duplicados:")
if not duplicados_cutter.empty:
    print(duplicados_cutter.head(10))  # Mostrar primeiros 10 duplicados

# Verificar valores nulos
print("\n\nVERIFICAÇÃO DE VALORES NULOS:")
print(f"\nCDD.xls - Valores nulos na coluna 'codigo': {df_cdd['codigo'].isna().sum()}")
print(f"CDD.xls - Valores nulos na coluna 'descricao': {df_cdd['descricao'].isna().sum()}")

print(f"\nCDU.xls - Valores nulos na coluna 'codigo': {df_cdu['codigo'].isna().sum()}")
print(f"CDU.xls - Valores nulos na coluna 'descricao': {df_cdu['descricao'].isna().sum()}")

print(f"\nCutter.xls - Valores nulos na coluna 'codigo': {df_cutter['codigo'].isna().sum()}")
print(f"Cutter.xls - Valores nulos na coluna 'descricao': {df_cutter['descricao'].isna().sum()}") 