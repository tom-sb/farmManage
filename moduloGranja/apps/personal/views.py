from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.views.generic import UpdateView, DeleteView
from apps.personal.models import Personal
from apps.clusters.models import Cluster
from .forms import FormPersonal
from django.template.loader import render_to_string

# Create your views here.
def index_personal(request):
    allpersonal = Personal.objects.all()
    persona = FormPersonal()
    contexto = {'personal':allpersonal,
                'form':persona}
    return render(request,'personal/index_personal.html', contexto)

def registrarPersonal(request):
    form = FormPersonal(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index_personal')
    else:
        return HttpResponse("Error de Validación")

"""
def editar_personal(request,pk):
    personal = get_object_or_404(Personal,pk=pk)
    template = 'personal/editar.html'
    form = FormPersonal(request.POST,instance=personal)
    if form.is_valid():
        personal = form.save()
        return redirect('index_personal')
    else:
        return HttpResponse("Error de Validación")
"""
class PersonalUpdateView(UpdateView):
    model = Personal 
    form_class = FormPersonal
    template_name = 'personal/editar.html'

    def dispatch(self, *args, **kwargs):
        self.personal_id = kwargs['pk']
        return super(PersonalUpdateView, self).dispatch(*args, **kwargs)

    
    def form_valid(self, form):
        form.save()
        personal = Personal.objects.get(id=self.personal_id)
        #return redirect('index_personal')
        return HttpResponse(render_to_string('personal/edit_success.html', {'personal':
            personal}))
    
class PersonalDeleteView(DeleteView):
    model = Personal
    template_name = 'personal/eliminar.html'

    #@method_decorator(permission_required('aidsbank.moderate_asset_comments'))
    def dispatch(self, *args, **kwargs):
        self.personal_id = kwargs['pk']
        return super(PersonalDeleteView, self).dispatch(*args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponse(render_to_string('personal/eliminar_success.html', {}))

    def get_context_data(self, **kwargs):
        context = super(PersonalDeleteView, self).get_context_data(**kwargs)
        personal = get_object_or_404(Personal, pk=self.personal_id)
        context['personal'] = personal

        return context

def eliminar_personals(request):
    listpersonal = request.POST.getlist('personal')
    template = 'personal/eliminarPersonals.html'
    personals = Personal.objects.filter(pk__in=[pk for pk in listpersonal])
    personals.delete()
    return redirect('index_personal')


def visualizarPersonal(request,pk):
    person = get_object_or_404(Personal,pk=pk)
    template = 'personal/visualizacion.html'
    clusters = person.cluster_set.all()
    context = {'personal':person,
            'clusters':clusters}
    return render(request,template,context)

def asignarCluster(request,pk):
    personal = get_object_or_404(Personal,pk=pk)

    template = "personal/asignarCluster.html"
    if request.method == 'POST':
        listcluster = request.POST.getlist('clusters')
        clusters = Cluster.objects.filter(pk__in=[nombre for nombre in listcluster])
        for cluster in clusters:
            cluster.personal.add(personal)
            cluster.save()
        return HttpResponse(render_to_string('personal/eliminar_success.html', {}))
    clusters = Cluster.objects.exclude(personal=personal.pk)
    #return redirect('asignarTareas',pk=pkP)
    context = {'personal':personal,
            'clusters':clusters}
    return render(request,template,context)


