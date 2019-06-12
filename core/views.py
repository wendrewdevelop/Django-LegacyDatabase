from django.shortcuts import render

from .forms import ProdutoForm
from .models import Produtos

def Produto(request):
   form = ProdutoForm(request.POST or None)
   listagem = Produtos.objects.all()

   if request.method == 'POST':
      if form.is_valid():
         form.save()
      else:
         form = ProdutoForm()
   else:
      form = ProdutoForm()

   params = {
      'form': form,
      'listagem': listagem
   }

   return render(request, 'produtos.html', params)   
