import os
import pandas as pd
from django.core.management.base import BaseCommand
from importacao.models import Secao, CDD, CDU, Cutter

class Command(BaseCommand):
    help = 'Importa dados das planilhas para o banco de dados'

    def handle(self, *args, **kwargs):
        # Caminho para as planilhas
        planilhas_dir = os.path.join(os.getcwd(), 'planilhas')
        
        try:
            # Importar Seções
            self.stdout.write('Importando seções...')
            df_secoes = pd.read_excel(os.path.join(planilhas_dir, 'secoes.xls'))
            self.stdout.write(f'Colunas encontradas na planilha de seções: {df_secoes.columns.tolist()}')
            
            for _, row in df_secoes.iterrows():
                Secao.objects.get_or_create(
                    nome=row['sessao']
                )

            # Importar CDD
            self.stdout.write('Importando CDD...')
            df_cdd = pd.read_excel(os.path.join(planilhas_dir, 'cdd.xls'))
            self.stdout.write(f'Colunas encontradas na planilha de CDD: {df_cdd.columns.tolist()}')
            
            for _, row in df_cdd.iterrows():
                CDD.objects.get_or_create(
                    codigo=row['Código'],
                    defaults={'descricao': row['Descrição']}
                )

            # Importar CDU
            self.stdout.write('Importando CDU...')
            df_cdu = pd.read_excel(os.path.join(planilhas_dir, 'cdu.xls'))
            self.stdout.write(f'Colunas encontradas na planilha de CDU: {df_cdu.columns.tolist()}')
            
            for _, row in df_cdu.iterrows():
                CDU.objects.get_or_create(
                    codigo=row['codigo'],
                    defaults={'descricao': row['descricao']}
                )

            # Importar Cutter
            self.stdout.write('Importando Cutter...')
            df_cutter = pd.read_excel(os.path.join(planilhas_dir, 'cutter.xls'))
            self.stdout.write(f'Colunas encontradas na planilha de Cutter: {df_cutter.columns.tolist()}')
            
            for _, row in df_cutter.iterrows():
                Cutter.objects.get_or_create(
                    codigo=row['codigo'],
                    defaults={'descricao': row['descricao']}
                )

            self.stdout.write(self.style.SUCCESS('Importação concluída com sucesso!'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Erro durante a importação: {str(e)}'))
            # Mostrar mais detalhes sobre o erro
            import traceback
            self.stdout.write(self.style.ERROR(traceback.format_exc())) 