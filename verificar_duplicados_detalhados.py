import pandas as pd

# Função para verificar duplicatas com detalhes
def verificar_duplicatas(df, nome_arquivo):
    print(f"\n=== {nome_arquivo} ===")
    
    # Agrupar por código e contar quantas descrições diferentes existem para cada código
    grupos = df.groupby('codigo')['descricao'].nunique().reset_index()
    grupos.columns = ['codigo', 'num_descricoes_diferentes']
    
    # Códigos com múltiplas descrições
    codigos_multi_descricao = grupos[grupos['num_descricoes_diferentes'] > 1]
    
    print(f"Total de códigos duplicados: {len(df[df.duplicated(subset=['codigo'], keep=False)])}")
    print(f"Códigos com descrições diferentes: {len(codigos_multi_descricao)}")
    print(f"Códigos com mesma descrição repetida: {len(df[df.duplicated(subset=['codigo'], keep=False)]) - len(codigos_multi_descricao)}")
    
    if len(codigos_multi_descricao) > 0:
        print("\nExemplos de códigos com descrições diferentes:")
        for i, row in codigos_multi_descricao.head(5).iterrows():
            codigo = row['codigo']
            print(f"\nCódigo: {codigo}")
            descricoes = df[df['codigo'] == codigo]['descricao'].tolist()
            for j, desc in enumerate(descricoes, 1):
                print(f"  {j}. {desc}")

# Analisar cada arquivo
arquivos = [
    ('CDD.xls', 'CDD'),
    ('CDU.xls', 'CDU'),
    ('Cutter.xls', 'Cutter')
]

print("ANÁLISE DETALHADA DE DUPLICIDADES\n")

for arquivo, nome in arquivos:
    df = pd.read_excel(arquivo)
    verificar_duplicatas(df, nome) 