import pandas as pd
import numpy as np
from collections import Counter

# Carregar as planilhas
df_secao = pd.read_excel('secao.xls')
df_cdd = pd.read_excel('CDD.xls')
df_cdu = pd.read_excel('CDU.xls')
df_cutter = pd.read_excel('Cutter.xls')

print("Comparando planilhas para identificar diferenças...")

# Verificar se CDD e CDU são iguais
if df_cdd.equals(df_cdu):
    print("CDD.xls e CDU.xls possuem EXATAMENTE os mesmos dados")
else:
    # Verificar diferenças específicas
    print("CDD.xls e CDU.xls são DIFERENTES")
    
    # Comparar cabeçalhos
    if sorted(df_cdd.columns.tolist()) == sorted(df_cdu.columns.tolist()):
        print("- Ambos têm as mesmas colunas:", df_cdd.columns.tolist())
    else:
        print("- Colunas diferentes:")
        print("  CDD:", df_cdd.columns.tolist())
        print("  CDU:", df_cdu.columns.tolist())
    
    # Verificar se os dados são os mesmos, mas em ordem diferente
    if df_cdd.shape == df_cdu.shape:
        print("- Ambos têm o mesmo número de linhas:", df_cdd.shape[0])
        
        # Verificar se os códigos são os mesmos
        cdd_codes = sorted(df_cdd['codigo'].tolist())
        cdu_codes = sorted(df_cdu['codigo'].tolist())
        
        if cdd_codes == cdu_codes:
            print("- Ambos contêm os mesmos códigos, possivelmente em ordem diferente")
        else:
            # Contar diferenças nos códigos
            cdd_counter = Counter(cdd_codes)
            cdu_counter = Counter(cdu_codes)
            
            cdd_only = cdd_counter - cdu_counter
            cdu_only = cdu_counter - cdd_counter
            
            if cdd_only:
                print(f"- {len(cdd_only)} códigos exclusivos em CDD.xls")
                print("  Exemplos:", list(cdd_only.keys())[:5])
            
            if cdu_only:
                print(f"- {len(cdu_only)} códigos exclusivos em CDU.xls")
                print("  Exemplos:", list(cdu_only.keys())[:5])
    else:
        print("- Número de linhas diferente:")
        print("  CDD:", df_cdd.shape[0])
        print("  CDU:", df_cdu.shape[0])

# Verificar se CDD e Cutter são iguais
if df_cdd.equals(df_cutter):
    print("\nCDD.xls e Cutter.xls possuem EXATAMENTE os mesmos dados")
else:
    # Verificar diferenças específicas
    print("\nCDD.xls e Cutter.xls são DIFERENTES")
    
    # Comparar cabeçalhos
    if sorted(df_cdd.columns.tolist()) == sorted(df_cutter.columns.tolist()):
        print("- Ambos têm as mesmas colunas:", df_cdd.columns.tolist())
    else:
        print("- Colunas diferentes:")
        print("  CDD:", df_cdd.columns.tolist())
        print("  Cutter:", df_cutter.columns.tolist())
    
    # Verificar se os dados são os mesmos, mas em ordem diferente
    if df_cdd.shape == df_cutter.shape:
        print("- Ambos têm o mesmo número de linhas:", df_cdd.shape[0])
        
        # Verificar se os códigos são os mesmos
        cdd_codes = sorted(df_cdd['codigo'].tolist())
        cutter_codes = sorted(df_cutter['codigo'].tolist())
        
        if cdd_codes == cutter_codes:
            print("- Ambos contêm os mesmos códigos, possivelmente em ordem diferente")
        else:
            # Contar diferenças nos códigos
            cdd_counter = Counter(cdd_codes)
            cutter_counter = Counter(cutter_codes)
            
            cdd_only = cdd_counter - cutter_counter
            cutter_only = cutter_counter - cdd_counter
            
            if cdd_only:
                print(f"- {len(cdd_only)} códigos exclusivos em CDD.xls")
                print("  Exemplos:", list(cdd_only.keys())[:5])
            
            if cutter_only:
                print(f"- {len(cutter_only)} códigos exclusivos em Cutter.xls")
                print("  Exemplos:", list(cutter_only.keys())[:5])
    else:
        print("- Número de linhas diferente:")
        print("  CDD:", df_cdd.shape[0])
        print("  Cutter:", df_cutter.shape[0])

# Verificar se CDU e Cutter são iguais
if df_cdu.equals(df_cutter):
    print("\nCDU.xls e Cutter.xls possuem EXATAMENTE os mesmos dados")
else:
    # Verificar diferenças específicas
    print("\nCDU.xls e Cutter.xls são DIFERENTES")
    
    # Comparar cabeçalhos
    if sorted(df_cdu.columns.tolist()) == sorted(df_cutter.columns.tolist()):
        print("- Ambos têm as mesmas colunas:", df_cdu.columns.tolist())
    else:
        print("- Colunas diferentes:")
        print("  CDU:", df_cdu.columns.tolist())
        print("  Cutter:", df_cutter.columns.tolist())
    
    # Verificar se os dados são os mesmos, mas em ordem diferente
    if df_cdu.shape == df_cutter.shape:
        print("- Ambos têm o mesmo número de linhas:", df_cdu.shape[0])
        
        # Verificar se os códigos são os mesmos
        cdu_codes = sorted(df_cdu['codigo'].tolist())
        cutter_codes = sorted(df_cutter['codigo'].tolist())
        
        if cdu_codes == cutter_codes:
            print("- Ambos contêm os mesmos códigos, possivelmente em ordem diferente")
        else:
            # Contar diferenças nos códigos
            cdu_counter = Counter(cdu_codes)
            cutter_counter = Counter(cutter_codes)
            
            cdu_only = cdu_counter - cutter_counter
            cutter_only = cutter_counter - cdu_counter
            
            if cdu_only:
                print(f"- {len(cdu_only)} códigos exclusivos em CDU.xls")
                print("  Exemplos:", list(cdu_only.keys())[:5])
            
            if cutter_only:
                print(f"- {len(cutter_only)} códigos exclusivos em Cutter.xls")
                print("  Exemplos:", list(cutter_only.keys())[:5])
    else:
        print("- Número de linhas diferente:")
        print("  CDU:", df_cdu.shape[0])
        print("  Cutter:", df_cutter.shape[0]) 