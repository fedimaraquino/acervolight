# AcervoLight - Sistema de Gerenciamento de Biblioteca

AcervoLight é um sistema web de gerenciamento de biblioteca e acervo escolar desenvolvido com Django, projetado para ser simples, leve e fácil de usar. Ideal para bibliotecas escolares, comunitárias ou pequenas instituições.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Django](https://img.shields.io/badge/Django-4.0%2B-green)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.2-purple)

## 🚀 Funcionalidades

### 📚 Gerenciamento de Livros
- Cadastro completo de livros com título, autor, editora e ano de publicação
- Classificação de livros por CDD, CDU, Cutter e Seções
- Busca avançada de livros por diferentes critérios
- Geração automática de código Cutter baseado no sobrenome do autor

### 👨‍🎓 Gerenciamento de Alunos
- Cadastro de alunos com dados completos (pessoais e escolares)
- Importação de alunos a partir de planilhas Excel
- Filtros avançados por gênero, raça/cor e outros critérios
- Interface amigável para visualização e edição de dados

### 🔍 Classificação Bibliográfica
- Suporte aos principais sistemas de classificação:
  - Sistema Decimal de Dewey (CDD)
  - Classificação Decimal Universal (CDU)
  - Tabela Cutter para códigos de autor
  - Seções personalizáveis

### 📊 Outras Funcionalidades
- Interface responsiva baseada em Bootstrap 5
- Personalização de colunas nas visualizações em lista
- Sistema de busca integrado
- Suporte à importação e exportação de dados

## 📋 Pré-requisitos

Para executar o AcervoLight, você precisará:

- Python 3.9+
- Django 4.0+
- Outras dependências listadas em `requirements.txt`

## 🔧 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/acervolight.git
   cd acervolight
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   
   # No Windows
   venv\Scripts\activate
   
   # No Linux/Mac
   source venv/bin/activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```

5. Crie um superusuário:
   ```bash
   python manage.py createsuperuser
   ```

6. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

7. Acesse http://127.0.0.1:8000/ no seu navegador.

## 📥 Importação de Dados

### Importando Alunos
Para importar alunos a partir de uma planilha Excel:

```bash
python manage.py importar_alunos caminho/para/alunos.xls
```

A planilha deve conter os seguintes campos (alguns são opcionais):
- inep_aluno: Código INEP do aluno
- nome: Nome completo do aluno (obrigatório)
- cpf: CPF do aluno
- dt_nascimento: Data de nascimento (formato YYYY-MM-DD)
- genero: Gênero (M ou F)
- raca: Raça/Cor (Branca, Preta, Parda, Amarela, Indígena, etc.)
- turma: Turma do aluno
- serie: Série/Ano escolar
- ano: Ano letivo
- logradouro: Endereço
- cidade: Cidade
- uf: Estado (UF)
- nome_mae: Nome da mãe
- nome_responsavel: Nome do responsável

## 🎨 Personalização

O AcervoLight foi projetado para ser altamente personalizável:

- Edite as templates em `importacao/templates/`
- Adicione seus estilos personalizados
- Modifique os modelos para atender às suas necessidades específicas

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Abrir issues para reportar bugs ou sugerir melhorias
2. Enviar pull requests com novas funcionalidades
3. Melhorar a documentação

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📞 Contato

Para dúvidas ou sugestões, entre em contato através das issues do GitHub ou por email.

---

Desenvolvido com ❤️ para facilitar o gerenciamento de acervos escolares e bibliotecas comunitárias. 