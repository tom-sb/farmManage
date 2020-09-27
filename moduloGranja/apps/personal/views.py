from django.shortcuts import render, redirect, get_object_or_404
from apps.personal.models import Personal
from apps.clusters.models import Cluster
from .forms import FormPersonal

# Create your views here.
def index_personal(request):
    allpersonal = Personal.objects.all()
    if request.method == 'POST':
        persona = FormPersonal(request.POST)
        if persona.is_valid():
            persona.save()
            return redirect('index_personal')
    else:
        persona = FormPersonal()
        contexto = {'personal':allpersonal,
                    'form':persona}
        return render(request,'personal/index_personal.html', contexto)

def editar_personal(request,pk):
    personal = get_object_or_404(Personal,pk=pk)
    template = 'personal/Registrar.html'
    if request.method == "POST":
        form = FormPersonal(request.POST,instance=personal)
        if form.is_valid():
            personal = form.save()
            return redirect('index_personal')
    else:
        form=FormPersonal(instance=personal)
    context = {'form':form}
    return render(request,template,context)

def eliminar_personal(request,pk):
    personal = get_object_or_404(Personal,pk=pk)
    personal.delete()
    return redirect('index_personal')

def visualizarPersonal(request,pk):
    personal = get_object_or_404(Personal,pk=pk)
    template = 'personal/visualizacion.html'
    clusters = Cluster.objects.filter(personal=personal.pk)
    context = {'personal':personal,
            'clusters':clusters}
    return render(request,template,context)

def asignarTareas(request,pk):
    personal = get_object_or_404(Personal,pk=pk)
    template = 'personal/asignar.html'
    clusters = Cluster.objects.exclude(personal=personal.pk)
    context = {'personal':personal,
            'clusters':clusters}

    return render(request,template,context)

def asignarCluster(request,pkP,pkC):
    personal = get_object_or_404(Personal,pk=pkP)
    cluster = get_object_or_404(Cluster,pk=pkC)
    cluster.personal.add(personal)
    cluster.save()
    return redirect('asignarTareas',pk=pkP)
