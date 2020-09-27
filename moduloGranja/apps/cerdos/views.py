from django.shortcuts import render, redirect, get_object_or_404
from apps.cerdos.models import Cerdo, Reproductora, Engorde,Nacido,Reproductor
from .forms import (FormCerdo, FormReproductora,FormEngorde,
            FormReproductor,FormNacido)
from apps.clusters.models import Cluster
from apps.farmacos.models import FichaMedicina, FichaVitamina, FichaVacuna
from apps.alimentos.models import FichaAlimento

# Create your views here.
def index_cerdos(request):
    allcerdos = Cerdo.objects.all()
    template = 'cerdos/index_cerdos.html'
    if request.method == 'POST':
        form = FormCerdo(request.POST)
        if form.is_valid():
            cerdo = form.save()
            return redirect('index_cerdos')
    else:
        form = FormCerdo()
        contexto = {'cerdos':allcerdos,
                'form':form,
                'nombre':'Cerdos'}
    return render(request,template, contexto)

def index_reproductora(request):
    allcerdos = Cerdo.objects.filter(pk__in=[r.pk for r in Reproductora.objects.all()])
    template = 'cerdos/index_cerdos.html'
    if request.method=='POST':
        form = FormCerdo(request.POST)
        if form.is_valid():
            cerdo=form.save()
            return redirect('index_reproductora')
    else:
        form = FormCerdo()
        context = {'cerdos':allcerdos,
                'form':form,
                'nombre':'Cerdo Reproductoras'}
    return render(request,template,context)
    
def index_nacido(request):
    allcerdos = Cerdo.objects.filter(pk__in=[r.pk for r in Nacido.objects.all()])
    template = 'cerdos/index_cerdos.html'
    if request.method=='POST':
        form = FormCerdo(request.POST)
        if form.is_valid():
            cerdo=form.save()
            return redirect('index_nacido')
    else:
        form = FormCerdo()
        context = {'cerdos':allcerdos,
                'form':form,
                'nombre':'Cerdo Nacido'}
    return render(request,template,context)
    
def index_engorde(request):
    allcerdos = Cerdo.objects.filter(pk__in=[r.pk for r in Engorde.objects.all()])
    template = 'cerdos/index_cerdos.html'
    if request.method=='POST':
        form = FormCerdo(request.POST)
        if form.is_valid():
            cerdo=form.save()
            return redirect('index_engorde')
    else:
        form = FormCerdo()
        context = {'cerdos':allcerdos,
                'form':form,
                'nombre':'Cerdo Engorde'}
    return render(request,template,context)
    
def index_reproductor(request):
    allcerdos = Cerdo.objects.filter(pk__in=[r.pk for r in Reproductor.objects.all()])
    template = 'cerdos/index_cerdos.html'
    if request.method=='POST':
        form = FormCerdo(request.POST)
        if form.is_valid():
            cerdo=form.save()
            return redirect('index_reproductor')
    else:
        form = FormCerdo()
        context = {'cerdos':allcerdos,
                'form':form,
                'nombre':'Cerdo Reproductor'}
    return render(request,template,context)


def visualizarCerdo(request,pk):
    cerdo = get_object_or_404(Cerdo,pk=pk)
    template= 'cerdos/visualizarCerdo.html'
    FichaMed = FichaMedicina.objects.filter(cerdo=cerdo)
    FichaVit = FichaVitamina.objects.filter(cerdo=cerdo)
    FichaVac = FichaVacuna.objects.filter(cerdo=cerdo)
    alimentos = FichaAlimento.objects.filter(cluster=cerdo.cluster)	
    context = {'cerdo':cerdo,
            'FichaMed':FichaMed,
            'FichaVit':FichaVit,
            'FichaVac':FichaVac,
            'alimentos':alimentos}

    return render(request,template,context)

def eliminarCerdo(request,pk):
    cerdo=get_object_or_404(Cerdo,pk=pk)
    cerdo.delete()
    return redirect('index_cerdos')

def RegistrarReproductor(request,pk):
    clusters = get_object_or_404(Cluster,pk=pk)
    if request.method == 'POST':
        cerdo = FormCerdo(request.POST)
        repro = FormReproductor(request.POST)
        if cerdo.is_valid() and repro.is_valid():
            cerd = cerdo.save(commit=False)
            cerd.cluster = clusters
            cerd.save()
            clusters.nro_cerdos +=1
            clusters.save()
            rep = repro.save(commit=False)
            rep.cerdo = cerd
            rep.save()
            return redirect('tablacluster',pk=clusters.pk)
    else:
        cerdo = FormCerdo()
        repro = FormReproductor()
        context = {'formcerdo':cerdo,
                'formrepro':repro}
    return render(request,'cerdos/Registrar.html',context)
    
