from django.shortcuts import render, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.
from .listar import ListarFacturas
from .models import Factura

path = 'static/facturas'

#for vector in ListarFacturas():
#   Factura.objects.create(nroFac1=vector[2],nroFac2=vector[3],
#   fecha=vector[4],RUC=vector[5],extra=vector[1],rucEmpresa=vector[0])

@login_required
def search(request):
    template='home/mostrar_facturas.html'
    if (request.GET.get('q') ):
        query=request.GET.get('q')

        result=Factura.objects.filter(Q(RUC=query) | Q(nroFac1=query) | 
        Q(nroFac2=query) | Q(fecha=query))
        paginate_by=10
        context={ 'posts':result 
        }
        return render(request,template,context)
    else:
       
        return redirect('home')
   

class PostListView(ListView):
    model = Factura
    template_name = 'home/mostrar_facturas.html'  # <app>/<model>_<viewtype>.html

    context_object_name = 'posts'
    ordering = ['-fecha']
    paginate_by = 10
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PostListView, self).dispatch(*args, **kwargs)
