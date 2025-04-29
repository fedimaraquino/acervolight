from django.core.management.base import BaseCommand
from importacao.models import Secao, CDD, CDU, Cutter

class Command(BaseCommand):
    help = 'Verifica o número de registros em cada tabela'

    def handle(self, *args, **kwargs):
        self.stdout.write(f'Total de registros na tabela Secao: {Secao.objects.count()}')
        self.stdout.write(f'Total de registros na tabela CDD: {CDD.objects.count()}')
        self.stdout.write(f'Total de registros na tabela CDU: {CDU.objects.count()}')
        self.stdout.write(f'Total de registros na tabela Cutter: {Cutter.objects.count()}') 