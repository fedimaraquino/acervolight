from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Secao, CDD, CDU, Cutter, Livro, Aluno
from .forms import LivroForm
import unicodedata

def home(request):
    secao_count = Secao.objects.count()
    cdd_count = CDD.objects.count()
    cdu_count = CDU.objects.count()
    cutter_count = Cutter.objects.count()
    livro_count = Livro.objects.count()
    
    context = {
        'secao_count': secao_count,
        'cdd_count': cdd_count,
        'cdu_count': cdu_count,
        'cutter_count': cutter_count,
        'livro_count': livro_count,
    }
    
    return render(request, 'importacao/home.html', context)

def secao_list(request):
    query = request.GET.get('q', '')
    
    if query:
        object_list = Secao.objects.filter(nome__icontains=query)
    else:
        object_list = Secao.objects.all()
    
    paginator = Paginator(object_list, 50)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'importacao/secao_list.html', {'page_obj': page_obj, 'query': query})

def cdd_list(request):
    query = request.GET.get('q', '')
    
    if query:
        object_list = CDD.objects.filter(Q(codigo__icontains=query) | Q(descricao__icontains=query))
    else:
        object_list = CDD.objects.all()
    
    paginator = Paginator(object_list, 50)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'importacao/cdd_list.html', {'page_obj': page_obj, 'query': query})

def cdu_list(request):
    query = request.GET.get('q', '')
    
    if query:
        object_list = CDU.objects.filter(Q(codigo__icontains=query) | Q(descricao__icontains=query))
    else:
        object_list = CDU.objects.all()
    
    paginator = Paginator(object_list, 50)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'importacao/cdu_list.html', {'page_obj': page_obj, 'query': query})

def cutter_list(request):
    query = request.GET.get('q', '')
    
    if query:
        object_list = Cutter.objects.filter(Q(codigo__icontains=query) | Q(descricao__icontains=query))
    else:
        object_list = Cutter.objects.all()
    
    paginator = Paginator(object_list, 50)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'importacao/cutter_list.html', {'page_obj': page_obj, 'query': query})

def livro_list(request):
    query = request.GET.get('q', '')
    
    # Colunas disponíveis para personalização
    colunas_disponiveis = {
        'titulo': 'Título',
        'autor': 'Autor',
        'ano_publicacao': 'Ano de Publicação',
        'editora': 'Editora',
        'secao': 'Seção',
        'cdd': 'CDD',
        'cdu': 'CDU',
        'cutter': 'Cutter',
    }
    
    # Verificar se há uma solicitação para salvar a configuração de colunas
    if request.method == 'POST' and 'salvar_colunas' in request.POST:
        colunas_selecionadas = request.POST.getlist('colunas')
        # Salvar na sessão
        request.session['livro_colunas'] = colunas_selecionadas
        # Redirecionar para a mesma página (GET) após processamento
        return redirect('importacao:livro_list')
    
    # Obter colunas da sessão ou usar o padrão
    colunas_selecionadas = request.session.get('livro_colunas', list(colunas_disponiveis.keys()))
    
    if query:
        object_list = Livro.objects.filter(
            Q(titulo__icontains=query) | 
            Q(autor__icontains=query) |
            Q(editora__icontains=query)
        )
    else:
        object_list = Livro.objects.all()
    
    # Adicionar o campo autor_sobrenome_inicial
    for livro in object_list:
        if livro.autor:
            # Dividir o nome do autor e pegar o último elemento
            partes_nome = livro.autor.split()
            if partes_nome:
                sobrenome = partes_nome[-1]
                # Pegar a primeira letra do sobrenome e converter para maiúscula
                livro.autor_sobrenome_inicial = sobrenome[0].upper() if sobrenome else ''
            else:
                livro.autor_sobrenome_inicial = ''
        else:
            livro.autor_sobrenome_inicial = ''
    
    paginator = Paginator(object_list, 20)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'importacao/livro_list.html', {
        'page_obj': page_obj, 
        'query': query,
        'colunas_disponiveis': colunas_disponiveis,
        'colunas_selecionadas': colunas_selecionadas
    })

def livro_create(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('importacao:livro_list')
    else:
        form = LivroForm()
    
    # Fornecer opções iniciais para os campos Select2
    secoes = Secao.objects.all()[:30]  # Limitar a 30 para não sobrecarregar
    cdds = CDD.objects.all()[:30]
    cdus = CDU.objects.all()[:30]
    cutters = Cutter.objects.all()[:30]
    
    return render(request, 'importacao/livro_form.html', {
        'form': form,
        'title': 'Cadastrar Novo Livro',
        'secoes': secoes,
        'cdds': cdds,
        'cdus': cdus, 
        'cutters': cutters
    })

def livro_update(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    
    # Adicionar o campo autor_sobrenome_inicial ao livro
    if livro.autor:
        # Dividir o nome do autor e pegar o último elemento
        partes_nome = livro.autor.split()
        if partes_nome:
            sobrenome = partes_nome[-1]
            # Pegar a primeira letra do sobrenome e converter para maiúscula
            livro.autor_sobrenome_inicial = sobrenome[0].upper() if sobrenome else ''
        else:
            livro.autor_sobrenome_inicial = ''
    else:
        livro.autor_sobrenome_inicial = ''
    
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('importacao:livro_list')
    else:
        form = LivroForm(instance=livro)
    
    # Fornecer opções iniciais para os campos Select2
    secoes = Secao.objects.all()[:30]  # Limitar a 30 para não sobrecarregar
    cdds = CDD.objects.all()[:30]
    cdus = CDU.objects.all()[:30]
    cutters = Cutter.objects.all()[:30]
    
    return render(request, 'importacao/livro_form.html', {
        'form': form,
        'title': 'Editar Livro',
        'livro': livro,
        'secoes': secoes,
        'cdds': cdds,
        'cdus': cdus, 
        'cutters': cutters
    })

def livro_delete(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    
    if request.method == 'POST':
        livro.delete()
        return redirect('importacao:livro_list')
    
    return render(request, 'importacao/livro_confirm_delete.html', {'livro': livro})

# APIs para busca de classificações
def api_search_secao(request):
    query = request.GET.get('q', '')
    if query:
        results = Secao.objects.filter(nome__icontains=query)[:20]
        data = [{'id': item.nome, 'text': item.nome} for item in results]
        return JsonResponse({'results': data})
    return JsonResponse({'results': []})

def api_search_cdd(request):
    query = request.GET.get('q', '')
    if query:
        results = CDD.objects.filter(
            Q(codigo__icontains=query) | Q(descricao__icontains=query)
        )[:20]
        data = [{'id': item.id, 'text': f"{item.codigo} - {item.descricao}"} for item in results]
        return JsonResponse({'results': data})
    return JsonResponse({'results': []})

def api_search_cdu(request):
    query = request.GET.get('q', '')
    if query:
        results = CDU.objects.filter(
            Q(codigo__icontains=query) | Q(descricao__icontains=query)
        )[:20]
        data = [{'id': item.id, 'text': f"{item.codigo} - {item.descricao}"} for item in results]
        return JsonResponse({'results': data})
    return JsonResponse({'results': []})

def api_search_cutter(request):
    query = request.GET.get('q', '')
    if query:
        results = Cutter.objects.filter(
            Q(codigo__icontains=query) | Q(descricao__icontains=query)
        )[:20]
        data = [{'id': item.id, 'text': f"{item.codigo} - {item.descricao}"} for item in results]
        return JsonResponse({'results': data})
    return JsonResponse({'results': []})

def api_gerar_cutter(request):
    sobrenome = request.GET.get('sobrenome', '').strip()
    if not sobrenome:
        return JsonResponse({'error': 'Sobrenome não fornecido'}, status=400)
    
    # Normalizar o sobrenome - remover acentos e converter para minúsculo
    sobrenome_normalizado = unicodedata.normalize('NFKD', sobrenome).encode('ASCII', 'ignore').decode('ASCII').lower()
    
    # Obtendo a primeira letra do sobrenome e convertendo para maiúscula
    primeira_letra = sobrenome[0].upper()
    
    # Obtendo a segunda letra do sobrenome
    segunda_letra = ''
    if len(sobrenome) > 1:
        segunda_letra = sobrenome[1].lower()
    
    # Obtendo a terceira letra do sobrenome (se existir)
    terceira_letra = ''
    if len(sobrenome) > 2:
        terceira_letra = sobrenome[2].lower()
    
    # Estratégias de busca em ordem de prioridade
    resultados = []
    
    # 1. Busca exata pela descrição do sobrenome
    cutters_descricao = Cutter.objects.filter(descricao__iexact=sobrenome).order_by('codigo')[:3]
    if cutters_descricao.exists():
        for cutter in cutters_descricao:
            # Criar notação completa: primeira letra do sobrenome + código Cutter
            codigo_completo = f"{primeira_letra}{cutter.codigo}"
            resultados.append({
                'id': cutter.id,
                'codigo': cutter.codigo,
                'descricao': cutter.descricao,
                'text': f"{codigo_completo} - {cutter.descricao}",
                'match_tipo': 'exato'
            })
    
    # 2. Busca pelo sobrenome que comece com o sobrenome fornecido
    if not resultados:
        cutters_comecam_com = Cutter.objects.filter(descricao__istartswith=sobrenome_normalizado).order_by('codigo')[:3]
        if cutters_comecam_com.exists():
            for cutter in cutters_comecam_com:
                # Criar notação completa: primeira letra do sobrenome + código Cutter
                codigo_completo = f"{primeira_letra}{cutter.codigo}"
                resultados.append({
                    'id': cutter.id,
                    'codigo': cutter.codigo,
                    'descricao': cutter.descricao,
                    'text': f"{codigo_completo} - {cutter.descricao}",
                    'match_tipo': 'comeca_com'
                })
    
    # 3. Busca por códigos que correspondam às primeiras letras do sobrenome
    if not resultados:
        # Código base com a primeira e segunda letra
        codigo_base = primeira_letra
        if segunda_letra:
            codigo_base += segunda_letra
        
        # Para mais precisão, adicionamos a terceira letra se disponível
        codigo_base_ext = codigo_base
        if terceira_letra:
            codigo_base_ext += terceira_letra
        
        # Primeiro tentamos com 3 letras
        cutters_codigo_3 = Cutter.objects.filter(codigo__startswith=codigo_base_ext).order_by('codigo')[:3]
        if cutters_codigo_3.exists():
            for cutter in cutters_codigo_3:
                # Criar notação completa: primeira letra do sobrenome + código Cutter
                codigo_completo = f"{primeira_letra}{cutter.codigo}"
                resultados.append({
                    'id': cutter.id,
                    'codigo': cutter.codigo,
                    'descricao': cutter.descricao,
                    'text': f"{codigo_completo} - {cutter.descricao}",
                    'match_tipo': 'codigo_3letras'
                })
        
        # Se não encontrar com 3 letras, tenta com 2
        if not resultados:
            cutters_codigo_2 = Cutter.objects.filter(codigo__startswith=codigo_base).order_by('codigo')[:3]
            if cutters_codigo_2.exists():
                for cutter in cutters_codigo_2:
                    # Criar notação completa: primeira letra do sobrenome + código Cutter
                    codigo_completo = f"{primeira_letra}{cutter.codigo}"
                    resultados.append({
                        'id': cutter.id,
                        'codigo': cutter.codigo,
                        'descricao': cutter.descricao,
                        'text': f"{codigo_completo} - {cutter.descricao}",
                        'match_tipo': 'codigo_2letras'
                    })
    
    # 4. Se tudo falhar, tenta apenas com a primeira letra
    if not resultados:
        cutters_primeira_letra = Cutter.objects.filter(codigo__startswith=primeira_letra).order_by('codigo')[:3]
        if cutters_primeira_letra.exists():
            for cutter in cutters_primeira_letra:
                # Criar notação completa: primeira letra do sobrenome + código Cutter
                codigo_completo = f"{primeira_letra}{cutter.codigo}"
                resultados.append({
                    'id': cutter.id,
                    'codigo': cutter.codigo,
                    'descricao': cutter.descricao,
                    'text': f"{codigo_completo} - {cutter.descricao}",
                    'match_tipo': 'primeira_letra'
                })
    
    # 5. Busca por similaridade no texto (usada como último recurso)
    if not resultados:
        from django.db.models import Value, CharField, F
        from django.db.models.functions import Concat, Length
        
        # Ordenado por comprimento da descrição para favorecer descrições mais curtas
        cutters_similar = Cutter.objects.annotate(
            len_desc=Length('descricao')
        ).filter(
            descricao__icontains=sobrenome[:3]
        ).order_by('len_desc')[:3]
        
        if cutters_similar.exists():
            for cutter in cutters_similar:
                # Criar notação completa: primeira letra do sobrenome + código Cutter
                codigo_completo = f"{primeira_letra}{cutter.codigo}"
                resultados.append({
                    'id': cutter.id,
                    'codigo': cutter.codigo,
                    'descricao': cutter.descricao,
                    'text': f"{codigo_completo} - {cutter.descricao}",
                    'match_tipo': 'similaridade'
                })
    
    return JsonResponse({'results': resultados})

def aluno_list(request):
    query = request.GET.get('q', '')
    genero_filter = request.GET.get('genero', '')
    raca_filter = request.GET.get('raca', '')
    
    # Colunas disponíveis para personalização
    colunas_disponiveis = {
        'nome': 'Nome',
        'cpf': 'CPF',
        'dt_nascimento': 'Data de Nascimento',
        'genero': 'Gênero',
        'raca': 'Raça/Cor',
        'turma': 'Turma',
        'serie': 'Série',
        'ano': 'Ano Letivo',
        'cidade': 'Cidade',
        'uf': 'UF',
    }
    
    # Verificar se há uma solicitação para salvar a configuração de colunas
    if request.method == 'POST' and 'salvar_colunas' in request.POST:
        colunas_selecionadas = request.POST.getlist('colunas')
        # Salvar na sessão
        request.session['aluno_colunas'] = colunas_selecionadas
        # Redirecionar para a mesma página (GET) após processamento
        return redirect('importacao:aluno_list')
    
    # Obter colunas da sessão ou usar o padrão
    colunas_selecionadas = request.session.get('aluno_colunas', list(colunas_disponiveis.keys()))
    
    # Aplicar filtros iniciais
    filters = Q()
    
    # Filtro por texto de busca
    if query:
        filters &= (
            Q(nome__icontains=query) | 
            Q(cpf__icontains=query) |
            Q(turma__icontains=query) |
            Q(serie__icontains=query) |
            Q(nome_mae__icontains=query) |
            Q(nome_responsavel__icontains=query)
        )
    
    # Filtro por gênero
    if genero_filter:
        filters &= Q(genero=genero_filter)
        
    # Filtro por raça
    if raca_filter:
        filters &= Q(raca=raca_filter)
    
    object_list = Aluno.objects.filter(filters)
    
    # Para os seletores de filtro
    generos_disponiveis = Aluno.GENERO_CHOICES
    racas_disponiveis = Aluno.RACA_CHOICES
    
    paginator = Paginator(object_list, 20)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'importacao/aluno_list.html', {
        'page_obj': page_obj, 
        'query': query,
        'genero_filter': genero_filter,
        'raca_filter': raca_filter,
        'generos_disponiveis': generos_disponiveis,
        'racas_disponiveis': racas_disponiveis,
        'colunas_disponiveis': colunas_disponiveis,
        'colunas_selecionadas': colunas_selecionadas
    })
