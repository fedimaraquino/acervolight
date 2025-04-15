from django.db import models

# Create your models here.

class Secao(models.Model):
    nome = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return self.nome

class CDD(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=20, db_index=True)
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.codigo} - {self.descricao}"

class CDU(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=20, db_index=True)
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.codigo} - {self.descricao}"

class Cutter(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=20, db_index=True)
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.codigo} - {self.descricao}"

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    ano_publicacao = models.IntegerField()
    editora = models.CharField(max_length=255)
    
    # Referências para as 4 tabelas
    secao = models.ForeignKey(Secao, on_delete=models.SET_NULL, null=True, blank=True)
    cdd = models.ForeignKey(CDD, on_delete=models.SET_NULL, null=True, blank=True)
    cdu = models.ForeignKey(CDU, on_delete=models.SET_NULL, null=True, blank=True)
    cutter = models.ForeignKey(Cutter, on_delete=models.SET_NULL, null=True, blank=True)
    
    data_cadastro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.ano_publicacao})"

class Aluno(models.Model):
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]
    
    RACA_CHOICES = [
        ('Branca', 'Branca'),
        ('Preta', 'Preta'),
        ('Parda', 'Parda'),
        ('Amarela', 'Amarela'),
        ('Indígena', 'Indígena'),
        ('Não declarada', 'Não declarada'),
    ]
    
    inep_aluno = models.BigIntegerField(null=True, blank=True, verbose_name="Código INEP")
    nome = models.CharField(max_length=255, verbose_name="Nome Completo")
    cpf = models.CharField(max_length=14, null=True, blank=True, verbose_name="CPF")
    dt_nascimento = models.DateField(null=True, blank=True, verbose_name="Data de Nascimento")
    nis = models.CharField(max_length=20, null=True, blank=True, verbose_name="NIS")
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES, null=True, blank=True, verbose_name="Gênero")
    raca = models.CharField(max_length=15, choices=RACA_CHOICES, null=True, blank=True, verbose_name="Raça/Cor")
    inep_escola = models.BigIntegerField(null=True, blank=True, verbose_name="Código INEP da Escola")
    turma = models.CharField(max_length=50, null=True, blank=True, verbose_name="Turma")
    serie = models.CharField(max_length=50, null=True, blank=True, verbose_name="Série")
    ano = models.IntegerField(null=True, blank=True, verbose_name="Ano Letivo")
    logradouro = models.CharField(max_length=255, null=True, blank=True, verbose_name="Logradouro")
    bairro = models.CharField(max_length=100, null=True, blank=True, verbose_name="Bairro")
    cidade = models.CharField(max_length=100, null=True, blank=True, verbose_name="Cidade")
    uf = models.CharField(max_length=2, null=True, blank=True, verbose_name="UF")
    nome_mae = models.CharField(max_length=255, null=True, blank=True, verbose_name="Nome da Mãe")
    nome_responsavel = models.CharField(max_length=255, null=True, blank=True, verbose_name="Nome do Responsável")
    
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")
    ultima_atualizacao = models.DateTimeField(auto_now=True, verbose_name="Última Atualização")
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"
        ordering = ['nome']
