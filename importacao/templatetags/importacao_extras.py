from django import template

register = template.Library()

@register.filter
def get_sobrenome(nome_completo):
    """
    Retorna o último nome de uma string (considerado como o sobrenome).
    """
    if not nome_completo:
        return ""
    
    partes_nome = nome_completo.split()
    if partes_nome:
        return partes_nome[-1]
    return ""

@register.filter
def primeira_letra(texto):
    """
    Retorna a primeira letra de um texto em maiúsculo.
    """
    if not texto:
        return ""
    
    if len(texto) > 0:
        return texto[0].upper()
    return "" 