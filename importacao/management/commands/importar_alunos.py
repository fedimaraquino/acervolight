import pandas as pd
from django.core.management.base import BaseCommand
from importacao.models import Aluno
from django.db import transaction

class Command(BaseCommand):
    help = 'Importa alunos da planilha Excel'

    def add_arguments(self, parser):
        parser.add_argument('arquivo_excel', type=str, help='Caminho para o arquivo Excel')

    def handle(self, *args, **options):
        arquivo_excel = options['arquivo_excel']
        self.stdout.write(self.style.SUCCESS(f'Iniciando importação do arquivo: {arquivo_excel}'))
        
        try:
            # Ler o arquivo Excel
            df = pd.read_excel(arquivo_excel)
            self.stdout.write(self.style.SUCCESS(f'Total de registros encontrados: {len(df)}'))
            
            # Normalizar os nomes das colunas
            # Algumas planilhas podem ter variações nos nomes das colunas
            df.columns = [col.lower().strip() for col in df.columns]
            
            # Mapeamento de possíveis variações nos nomes das colunas
            mapeamento_colunas = {
                'inep_aluno': ['inep_aluno', 'inep', 'codigo_inep'],
                'nome': ['nome', 'aluno'],
                'cpf': ['cpf'],
                'dt_nascimento': ['dt_nascimento', 'data_nascimento', 'nascimento'],
                'nis': ['nis'],
                'genero': ['genero', 'sexo'],
                'raca': ['raça', 'raca', 'cor'],
                'inep_escola': ['inep_escola', 'escola_inep'],
                'turma': ['turma'],
                'serie': ['serie', 'série'],
                'ano': ['ano', 'ano_letivo'],
                'logradouro': ['logradoura', 'logradouro', 'endereco', 'endereço'],
                'bairro': ['bairro'],
                'cidade': ['cidade', 'municipio', 'município'],
                'uf': ['uf', 'estado'],
                'nome_mae': ['nome_mae', 'mae', 'mãe'],
                'nome_responsavel': ['nome_responsavel', 'responsavel', 'responsável']
            }
            
            # Normalizar as colunas da planilha para o nome padrão usado no modelo
            colunas_normalizadas = {}
            for nome_padrao, possiveis_nomes in mapeamento_colunas.items():
                for possivel_nome in possiveis_nomes:
                    if possivel_nome in df.columns:
                        colunas_normalizadas[possivel_nome] = nome_padrao
                        break
            
            # Renomear as colunas
            if colunas_normalizadas:
                df = df.rename(columns=colunas_normalizadas)
            
            # Contadores
            contador_novos = 0
            contador_atualizados = 0
            contador_erros = 0
            
            # Processar em transação para garantir a consistência
            with transaction.atomic():
                for i, row in df.iterrows():
                    try:
                        # Verificar se o aluno já existe pelo INEP ou CPF
                        aluno = None
                        inep = row.get('inep_aluno')
                        cpf = row.get('cpf')
                        
                        if pd.notna(inep) and inep:
                            try:
                                aluno = Aluno.objects.filter(inep_aluno=inep).first()
                            except (ValueError, TypeError):
                                pass
                        
                        if not aluno and pd.notna(cpf) and cpf:
                            aluno = Aluno.objects.filter(cpf=cpf).first()
                        
                        # Preparar dados
                        dados = {
                            'nome': str(row.get('nome', '')).strip() if pd.notna(row.get('nome', '')) else '',
                            'cpf': str(row.get('cpf', '')).strip() if pd.notna(row.get('cpf', '')) else None,
                            'nis': str(row.get('nis', '')).strip() if pd.notna(row.get('nis', '')) else None,
                            'genero': str(row.get('genero', '')).strip()[0].upper() if pd.notna(row.get('genero', '')) and row.get('genero', '') else None,
                            'raca': str(row.get('raca', '')).strip().capitalize() if pd.notna(row.get('raca', '')) else None,
                            'turma': str(row.get('turma', '')).strip() if pd.notna(row.get('turma', '')) else None,
                            'serie': str(row.get('serie', '')).strip() if pd.notna(row.get('serie', '')) else None,
                            'logradouro': str(row.get('logradouro', '')).strip() if pd.notna(row.get('logradouro', '')) else None,
                            'bairro': str(row.get('bairro', '')).strip() if pd.notna(row.get('bairro', '')) else None,
                            'cidade': str(row.get('cidade', '')).strip() if pd.notna(row.get('cidade', '')) else None,
                            'uf': str(row.get('uf', '')).strip().upper() if pd.notna(row.get('uf', '')) else None,
                            'nome_mae': str(row.get('nome_mae', '')).strip() if pd.notna(row.get('nome_mae', '')) else None,
                            'nome_responsavel': str(row.get('nome_responsavel', '')).strip() if pd.notna(row.get('nome_responsavel', '')) else None,
                        }
                        
                        # Tratar campos numéricos e data
                        if pd.notna(row.get('inep_aluno', '')):
                            try:
                                dados['inep_aluno'] = int(row.get('inep_aluno'))
                            except (ValueError, TypeError):
                                dados['inep_aluno'] = None
                        
                        if pd.notna(row.get('inep_escola', '')):
                            try:
                                dados['inep_escola'] = int(row.get('inep_escola'))
                            except (ValueError, TypeError):
                                dados['inep_escola'] = None
                        
                        if pd.notna(row.get('ano', '')):
                            try:
                                dados['ano'] = int(row.get('ano'))
                            except (ValueError, TypeError):
                                dados['ano'] = None
                        
                        if pd.notna(row.get('dt_nascimento', '')):
                            dados['dt_nascimento'] = row.get('dt_nascimento')
                        
                        # Criar ou atualizar aluno
                        if aluno:
                            for key, value in dados.items():
                                setattr(aluno, key, value)
                            aluno.save()
                            contador_atualizados += 1
                        else:
                            if dados['nome']:  # Nome é obrigatório
                                Aluno.objects.create(**dados)
                                contador_novos += 1
                            else:
                                contador_erros += 1
                                self.stdout.write(self.style.WARNING(f'Linha {i+2}: Nome não fornecido, registro ignorado.'))
                    
                    except Exception as e:
                        contador_erros += 1
                        self.stdout.write(self.style.ERROR(f'Erro ao processar linha {i+2}: {str(e)}'))
            
            self.stdout.write(self.style.SUCCESS(f'Importação concluída!'))
            self.stdout.write(self.style.SUCCESS(f'Total de alunos criados: {contador_novos}'))
            self.stdout.write(self.style.SUCCESS(f'Total de alunos atualizados: {contador_atualizados}'))
            self.stdout.write(self.style.WARNING(f'Total de erros: {contador_erros}'))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Erro ao processar o arquivo: {str(e)}')) 