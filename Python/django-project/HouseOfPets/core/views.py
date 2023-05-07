from django.shortcuts import render
from core.forms import ContatoForm
from core.forms import ReservaForm

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')
    
def contato(request):
    #{%csrf_token%} é um template para não deixar qualquer injetar codigo no seu 
    # dentro do arquivo HTML:
    # {{ Server para localizar a variavel que foi passada no context}} 
    # | serve para utilizar o filtro, por exemplo {{ nome|upper }} -> transforma o nome em maiúsculo
    sucesso = False
    print(sucesso);

    if request.method == 'GET':
      print("iniciando formulario")      
      form = ContatoForm()
    else:
      print(request)        
      form = ContatoForm(request.POST)
      if form.is_valid():
        sucesso = True
    
    context = {
        'nome': 'Ednesio Colli',
        'telefone': '(49) 988369338',
        'formulario': form,
        'sucesso': sucesso
    }
    
    return render(request, 'contato.html', context)

def reserva(request):
    sucesso = False

    if request.method == 'GET':      
      form = ReservaForm()
    else:
      form = ReservaForm(request.POST)
      if form.is_valid():
        sucesso = True

    
    context = {
        'formulario': form,
        'sucesso': sucesso
    }
    
    return render(request, 'reserva.html', context)


def sobre(request):
    return render(request, 'about.html')