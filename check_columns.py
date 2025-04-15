import pandas as pd

files = ['secao.xls', 'CDD.xls', 'CDU.xls', 'Cutter.xls']

for file in files:
    print(f"\nArquivo: {file}")
    df = pd.read_excel(file)
    print(f"Colunas: {df.columns.tolist()}")
    print(f"Primeiras linhas:")
    print(df.head()) 