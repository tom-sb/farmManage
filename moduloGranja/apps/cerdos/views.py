from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib import messages
from apps.cerdos.models import Cerdo,Raza, Reproductora, Engorde,Nacido,Reproductor
from .forms import FormCerdo,FormRaza,FormReproductora,FormEngorde,FormReproductor,FormNacido
from apps.clusters.models import Cluster,CerdoCluster
from apps.farmacos.models import FichaMedicina, FichaVitamina, FichaVacuna
from apps.alimentos.models import FichaAlimento
from django.template.loader import render_to_string

# Create your views here.
def index_cerdos(request):
    allcerdos = Cerdo.objects.all()
    allrazas = Raza.objects.all()
    template = 'cerdos/homeCerdos.html'
    formcerdo = FormCerdo
    formraza = FormRaza
    contexto = {'cerdos':allcerdos,
                'razas':allrazas,
                'form':formcerdo,
                'r_form':formraza}
    return render(request,template, contexto)

def registrarCerdo(request):
    form = FormCerdo(request.POST)
    if form.is_valid() :
        form.save()
        return redirect('index_cerdos')
    else:
        return HttpResponse("Error de Validación")

def registrarRaza(request):
    if request.method == 'POST':
        form = FormRaza(request.POST)
        if form.is_valid():
            raza = form.save()
            return redirect('index_cerdos')
        else:
            return HttpResponse("Error de Validación")
    return redirect('/')

def eliminarCerdo(request):
    listinputs=request.POST.getlist('foo')
    cerdos = Cerdo.objects.filter(pk__in=[nombre for nombre in listinputs])
    #cerdos.delete()
    #return HttpResponse(render_to_string('personal/eliminar_success.html',{}))
    template ="personal/eliminar_success.html"
    context = {
            'cerdos':cerdos}
    return render(request,template,context)

def determinarGalpon(request,pk):
    cluster = get_object_or_404(Cluster,pk=pk)
    listinputs=request.POST.getlist('foo')
    cerdos = Cerdo.objects.filter(pk__in=[nombre for nombre in listinputs])
    for cerdo in cerdos:
        CerdoCluster.objects.create(cerdo=cerdo,galpon=cluster)

    return redirect('index_cerdos')

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
    
