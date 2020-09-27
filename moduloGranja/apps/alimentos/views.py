from django.shortcuts import render, redirect, get_object_or_404

from .forms import FormAlimento, FormFichaAlimento
from .models import Alimento, FichaAlimento


# Create your views here.
def index_alimentos(request):
	allalimentos = Alimento.objects.all()
	if request.method == 'POST':
		alimento = FormAlimento(request.POST)
		if alimento.is_valid():
			alimento.save()
			return redirect('index_alimentos')
	else:
		alimento = FormAlimento()
		contexto = {'alimentos':allalimentos, 'form':alimento}
		return render(request,'alimentos/index_alimentos.html',contexto)

def editarAlimento(request,pk):
	alimento = get_object_or_404(Alimento,pk=pk)
	template='alimentos/Registrar.html'
	if request.method == 'POST':
		form = FormAlimento(request.POST, instance=alimento)
		if form.is_valid():
			alimento = form.save()
			return redirect('index_alimentos')
	else:
		form=FormAlimento(instance=alimento)
	context = {'form':form}
	return render(request,template,context)

def eliminarAlimento(request,pk):
	alimento = get_object_or_404(Alimento,pk=pk)
	alimento.delete()
	return redirect('index_alimentos')

def visualizarAlimento(request,pk):
	alimento = get_object_or_404(Alimento,pk=pk)
	template = 'alimentos/visualizacion.html'
	ficha_alimento = FichaAlimento.objects.filter(alimento=alimento.pk)
	context = {'alimento':alimento, 'ficha_alimento':ficha_alimento}
	return render(request,template,context)
#############################################################

def ficha_alimento(request):
	allficha_alimentos = FichaAlimento.objects.all()
	if request.method == 'POST':
		alimento = FormFichaAlimento(request.POST)
		if alimento.is_valid():
			alimento.save()
			return redirect('ficha_alimento')
	else:
		alimento = FormFichaAlimento()
		contexto = {'ficha_alimento':allficha_alimentos, 'form':alimento}
		return render(request,'fichas/ficha_alimento.html',contexto)

def ficha_alimento_editar(request,pk):
	alimento = get_object_or_404(FichaAlimento,pk=pk)
	template='alimentos/Registrar.html'
	if request.method == 'POST':
		form = FormFichaAlimento(request.POST, instance=alimento)
		if form.is_valid():
			alimento = form.save()
			return redirect('ficha_alimento')
	else:
		form=FormFichaAlimento(instance=alimento)
	context = {'form':form}
	return render(request,template,context)

def ficha_alimento_eliminar(request,pk):
	alimento = get_object_or_404(FichaAlimento,pk=pk)
	alimento.delete()
	return redirect('ficha_alimento')

def ficha_alimento_visualizar(request,pk):
	alimento = get_object_or_404(FichaAlimento,pk=pk)
	template = 'alimentos/visualizacion.html'
	ficha_alimento = FichaFichaAlimento.objects.filter(alimento=alimento.pk)
	context = {'alimento':alimento, 'ficha_alimento':ficha_alimento}
	return render(request,template,context)

############################################################

def registrarAlimento(request):
    if request.method == 'POST':
        alimento = FormAlimento(request.POST)
        if alimento.is_valid():
            alimento.save()
            return redirect('index_alimentos')
    else:
        alimento = FormAlimento()
    return render(request,'alimentos/Registrar.html',{'form':alimento})

def registrarFicha(request):
    if request.method == 'POST':
        ficha = FormFichaAlimento(request.POST)
        if ficha.is_valid():
            ficha.save()
            return redirect('index_alimentos')
    else:
        ficha=FormFichaAlimento()
    return render(request,'alimentos/Registrar.html',{'form':ficha})

