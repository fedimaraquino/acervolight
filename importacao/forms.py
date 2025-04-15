from django import forms
from .models import Livro, Secao, CDD, CDU, Cutter

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'ano_publicacao', 'editora', 'secao', 'cdd', 'cdu', 'cutter']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'ano_publicacao': forms.NumberInput(attrs={'class': 'form-control'}),
            'editora': forms.TextInput(attrs={'class': 'form-control'}),
            # Não definimos widgets para os campos select, pois usamos Select2 no template
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Inicialmente não limitamos as queryset, permitindo que qualquer valor seja validado
        # O Select2 irá buscar os valores conforme necessário
        
        # Se já existe uma instância, garantir que os valores atuais estejam nas querysets
        if 'instance' in kwargs and kwargs['instance']:
            instance = kwargs['instance']
            if instance.secao:
                self.fields['secao'].queryset = Secao.objects.filter(pk=instance.secao.pk)
            if instance.cdd:
                self.fields['cdd'].queryset = CDD.objects.filter(pk=instance.cdd.pk)
            if instance.cdu:
                self.fields['cdu'].queryset = CDU.objects.filter(pk=instance.cdu.pk)
            if instance.cutter:
                self.fields['cutter'].queryset = Cutter.objects.filter(pk=instance.cutter.pk)
    
    def clean_secao(self):
        secao_id = self.cleaned_data.get('secao')
        if secao_id:
            # Para secao, o valor já é a chave primária (nome)
            # Apenas verificamos se existe
            try:
                return Secao.objects.get(pk=secao_id)
            except Secao.DoesNotExist:
                raise forms.ValidationError("Seção inválida")
        return None
    
    def clean_cdd(self):
        cdd_id = self.cleaned_data.get('cdd')
        if cdd_id:
            try:
                # Verifica se o valor é um número inteiro (ID)
                try:
                    cdd_id = int(cdd_id)
                except (ValueError, TypeError):
                    # Se não for um número, o Select2 provavelmente está enviando o objeto
                    # No caso do CDD, vamos extrair o ID
                    if hasattr(cdd_id, 'id'):
                        cdd_id = cdd_id.id
                    else:
                        raise forms.ValidationError("CDD inválido: formato incorreto")
                
                # Agora verificamos se o ID existe
                return CDD.objects.get(pk=cdd_id)  # Retorna o objeto completo
            except CDD.DoesNotExist:
                raise forms.ValidationError("CDD inválido")
        return None
    
    def clean_cdu(self):
        cdu_id = self.cleaned_data.get('cdu')
        if cdu_id:
            try:
                # Verifica se o valor é um número inteiro (ID)
                try:
                    cdu_id = int(cdu_id)
                except (ValueError, TypeError):
                    # Se não for um número, o Select2 provavelmente está enviando o objeto
                    # No caso do CDU, vamos extrair o ID
                    if hasattr(cdu_id, 'id'):
                        cdu_id = cdu_id.id
                    else:
                        raise forms.ValidationError("CDU inválido: formato incorreto")
                
                # Agora verificamos se o ID existe
                return CDU.objects.get(pk=cdu_id)  # Retorna o objeto completo
            except CDU.DoesNotExist:
                raise forms.ValidationError("CDU inválido")
        return None
    
    def clean_cutter(self):
        cutter_id = self.cleaned_data.get('cutter')
        if cutter_id:
            try:
                # Verifica se o valor é um número inteiro (ID)
                try:
                    cutter_id = int(cutter_id)
                except (ValueError, TypeError):
                    # Se não for um número, o Select2 provavelmente está enviando o objeto
                    # No caso do Cutter, vamos extrair o ID
                    if hasattr(cutter_id, 'id'):
                        cutter_id = cutter_id.id
                    else:
                        raise forms.ValidationError("Cutter inválido: formato incorreto")
                
                # Agora verificamos se o ID existe
                return Cutter.objects.get(pk=cutter_id)  # Retorna o objeto completo
            except Cutter.DoesNotExist:
                raise forms.ValidationError("Cutter inválido")
        return None 