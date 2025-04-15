import os
import pandas as pd
from django.core.management.base import BaseCommand
from importacao.models import Secao, CDD, CDU, Cutter

class Command(BaseCommand):
    help = 'Importa dados das planilhas para o banco de dados'

    def handle(self, *args, **options):
        # Limpar todas as tabelas antes de importar
        self.stdout.write(self.style.WARNING('Limpando tabelas existentes...'))
        Secao.objects.all().delete()
        CDD.objects.all().delete()
        CDU.objects.all().delete()
        Cutter.objects.all().delete()
        
        # Importar dados da planilha secoes.xls
        try:
            df_secao = pd.read_excel('secoes.xls')
            # Verificar se as colunas necessárias existem
            if 'sessao' in df_secao.columns:  # Nome da coluna é 'sessao'
                total_rows = 0
                imported_rows = 0
                for _, row in df_secao.iterrows():
                    if pd.notna(row['sessao']):  # Verificar se o valor não é NaN
                        total_rows += 1
                        try:
                            Secao.objects.create(nome=str(row['sessao']))
                            imported_rows += 1
                        except Exception as e:
                            self.stdout.write(self.style.WARNING(f'Erro ao importar linha da seção: {e}'))
                
                self.stdout.write(self.style.SUCCESS(f'Dados da seção importados com sucesso! ({imported_rows}/{total_rows} registros)'))
            else:
                self.stdout.write(self.style.WARNING('Colunas necessárias não encontradas em secoes.xls'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Erro ao importar dados da seção: {e}'))

        # Importar dados da planilha CDD.xls para a tabela CDD
        try:
            df_cdd = pd.read_excel('CDD.xls')
            if 'Código' in df_cdd.columns and 'Descrição' in df_cdd.columns:  # Nomes das colunas em CDD
                total_rows = 0
                imported_rows = 0
                for _, row in df_cdd.iterrows():
                    if pd.notna(row['Código']) and pd.notna(row['Descrição']):
                        total_rows += 1
                        try:
                            CDD.objects.create(
                                codigo=str(row['Código']),
                                descricao=str(row['Descrição'])
                            )
                            imported_rows += 1
                        except Exception as e:
                            self.stdout.write(self.style.WARNING(f'Erro ao importar linha do CDD: {e}'))
                
                self.stdout.write(self.style.SUCCESS(f'Dados do CDD importados com sucesso! ({imported_rows}/{total_rows} registros)'))
            else:
                self.stdout.write(self.style.WARNING('Colunas necessárias não encontradas em CDD.xls'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Erro ao importar dados do CDD: {e}'))

        # Importar dados da planilha CDU.xls para a tabela CDU
        try:
            df_cdu = pd.read_excel('CDU.xls')
            if 'codigo' in df_cdu.columns and 'descricao' in df_cdu.columns:  # Nomes das colunas em CDU
                total_rows = 0
                imported_rows = 0
                for _, row in df_cdu.iterrows():
                    if pd.notna(row['codigo']) and pd.notna(row['descricao']):
                        total_rows += 1
                        try:
                            CDU.objects.create(
                                codigo=str(row['codigo']),
                                descricao=str(row['descricao'])
                            )
                            imported_rows += 1
                        except Exception as e:
                            self.stdout.write(self.style.WARNING(f'Erro ao importar linha do CDU: {e}'))
                
                self.stdout.write(self.style.SUCCESS(f'Dados do CDU importados com sucesso! ({imported_rows}/{total_rows} registros)'))
            else:
                self.stdout.write(self.style.WARNING('Colunas necessárias não encontradas em CDU.xls'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Erro ao importar dados do CDU: {e}'))

        # Importar dados da planilha Cutter.xls para a tabela Cutter
        try:
            df_cutter = pd.read_excel('Cutter.xls')
            if 'codigo' in df_cutter.columns and 'descricao' in df_cutter.columns:  # Nomes das colunas em Cutter
                total_rows = 0
                imported_rows = 0
                for _, row in df_cutter.iterrows():
                    if pd.notna(row['codigo']) and pd.notna(row['descricao']):
                        total_rows += 1
                        try:
                            Cutter.objects.create(
                                codigo=str(row['codigo']),
                                descricao=str(row['descricao'])
                            )
                            imported_rows += 1
                        except Exception as e:
                            self.stdout.write(self.style.WARNING(f'Erro ao importar linha do Cutter: {e}'))
                
                self.stdout.write(self.style.SUCCESS(f'Dados do Cutter importados com sucesso! ({imported_rows}/{total_rows} registros)'))
            else:
                self.stdout.write(self.style.WARNING('Colunas necessárias não encontradas em Cutter.xls'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Erro ao importar dados do Cutter: {e}')) 