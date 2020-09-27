from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .forms import FormCluster
from .models import Cluster
from apps.cerdos.models import Cerdo
from apps.personal.models import Personal
from apps.alimentos.models import FichaAlimento

from django.db.models import Q

# Create your views here.
def index_clusters(request):
    template = 'clusters/index_clusters.html'
    clusters = Cluster.objects.all()
    if request.method == 'POST':
        cluster=FormCluster(request.POST)
        if cluster.is_valid():
            cluster.save()
            return redirect('index_cluster')
    else:
        cluster = FormCluster()
        context = {'clusters':clusters,
                'form':cluster}
    return render(request,template,context)

def tablacluster(request,pk):
    clust = get_object_or_404(Cluster, pk=pk)
    cerdos = Cerdo.objects.filter(Q(cluster=pk))
    alimentos = FichaAlimento.objects.filter(Q(cluster=pk))
    template = 'clusters/tabla.html'
    context = {'cerdos':cerdos,
            'cluster':clust,
            'alimentos':alimentos}
    return render(request,template,context)

def asignarPersonal(request,pk,status):
    clust =  get_object_or_404(Cluster,pk=pk)
    template = "clusters/asignarPersonal.html"

    if status==0:
        personal=Personal.objects.exclude(id__in=[p.id for p in clust.personal.all()])
        personalC=Personal.objects.filter(id__in=[p.id for p in clust.personal.all()])
        context = {'cluster':clust,
                'personal':personal,
                'personalC':personalC,
                'status':status,
                'active1':'active'}
    elif status==1:
        cerdosC=Cerdo.objects.filter(Q(cluster=pk))
        cerdos=Cerdo.objects.exclude(cluster__in=[c.pk for c in Cluster.objects.all()])
        context = {'cluster':clust,
                'cerdosC':cerdosC,
                'cerdos':cerdos,
                'status':status,
                'active2':'active'}
    else:
        context ={'cluster':clust}
    return render(request,template,context)

def removerPersonal(request,pkC,pkP):
    cluster = get_object_or_404(Cluster,pk=pkC)
    personal = get_object_or_404(Personal,pk=pkP)
    cluster.personal.remove(personal)
    cluster.save()

    return redirect('asignarPersonal',pk=cluster.pk,status=0)

def insertPersonal(request,pkC,pkP):
    cluster = get_object_or_404(Cluster,pk=pkC)
    personal = get_object_or_404(Personal,pk=pkP)
    cluster.personal.add(personal)
    cluster.save()

    return redirect('asignarPersonal',pk=cluster.pk,status=0)

def removeCerdo(request,pkC,pkc):
    cluster = get_object_or_404(Cluster,pk=pkC)
    cerdo = get_object_or_404(Cerdo,pk=pkc)
    cluster.cerdo_set.remove(cerdo)

    return redirect('asignarPersonal',pk=cluster.pk,status=1)
    
def insertCerdo(request,pkC,pkc):
    cluster= get_object_or_404(Cluster,pk=pkC)
    cerdo = get_object_or_404(Cerdo,pk=pkc)
    cluster.cerdo_set.add(cerdo)
    return redirect('asignarPersonal',pk=cluster.pk,status=1)
