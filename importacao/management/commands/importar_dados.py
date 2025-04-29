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
            # Limpar todas as tabelas antes de importar
            Secao.objects.all().delete()
            CDD.objects.all().delete()
            CDU.objects.all().delete()
            Cutter.objects.all().delete()
            self.stdout.write('Tabelas limpas. Iniciando nova importação...')

            # Importar Seções
            self.stdout.write('Importando seções...')
            df_secoes = pd.read_excel(os.path.join(planilhas_dir, 'secoes.xls'))
            self.stdout.write(f'Colunas encontradas na planilha de seções: {df_secoes.columns.tolist()}')
            self.stdout.write(f'Total de registros na planilha Seções: {len(df_secoes)}')
            
            for _, row in df_secoes.iterrows():
                Secao.objects.create(
                    nome=row['sessao']
                )

            # Importar CDD
            self.stdout.write('Importando CDD...')
            df_cdd = pd.read_excel(os.path.join(planilhas_dir, 'cdd.xls'))
            self.stdout.write(f'Colunas encontradas na planilha de CDD: {df_cdd.columns.tolist()}')
            self.stdout.write(f'Total de registros na planilha CDD: {len(df_cdd)}')
            
            for _, row in df_cdd.iterrows():
                CDD.objects.create(
                    codigo=row['Código'],
                    descricao=row['Descrição']
                )

            # Importar CDU
            self.stdout.write('Importando CDU...')
            df_cdu = pd.read_excel(os.path.join(planilhas_dir, 'cdu.xls'))
            self.stdout.write(f'Colunas encontradas na planilha de CDU: {df_cdu.columns.tolist()}')
            self.stdout.write(f'Total de registros na planilha CDU: {len(df_cdu)}')
            
            for _, row in df_cdu.iterrows():
                CDU.objects.create(
                    codigo=row['codigo'],
                    descricao=row['descricao']
                )

            # Importar Cutter
            self.stdout.write('Importando Cutter...')
            df_cutter = pd.read_excel(os.path.join(planilhas_dir, 'cutter.xls'))
            self.stdout.write(f'Colunas encontradas na planilha de Cutter: {df_cutter.columns.tolist()}')
            self.stdout.write(f'Total de registros na planilha Cutter: {len(df_cutter)}')
            
            for _, row in df_cutter.iterrows():
                Cutter.objects.create(
                    codigo=row['codigo'],
                    descricao=row['descricao']
                )

            self.stdout.write(self.style.SUCCESS('Importação concluída com sucesso!'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Erro durante a importação: {str(e)}'))
            # Mostrar mais detalhes sobre o erro
            import traceback
            self.stdout.write(self.style.ERROR(traceback.format_exc())) 