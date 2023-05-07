from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail')
    mensagem = forms.CharField(widget=forms.Textarea, label='Observação', max_length=500)
    
class ReservaForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    telefone = forms.CharField(label='Telefone', max_length=100)
    data = forms.DateField(widget=forms.widgets.DateInput(attrs={'type':'date'}), label="Data da reserva")
    horario = forms.TimeField(widget=forms.widgets.TimeInput(attrs={'type':'time'}), label="Hora da reserva")
    observacoes = forms.CharField(widget=forms.Textarea, label='Observação', max_length=500)
