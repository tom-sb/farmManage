from django.shortcuts import render, redirect, get_object_or_404

from .forms import (
        FormVacuna,FormVitamina,FormMedicina,
        FormFichaMedicina,FormFichaVitamina,FormFichaVacuna
)
from .models import (
		Vacuna, Vitamina, Medicina,
		FichaVet, FichaMedicina,
		FichaVitamina, FichaVacuna
)

# Create your views here.

def index_medicinas(request):
	allmedicinas = Medicina.objects.all()
	if request.method == 'POST':
		medicina = FormMedicina(request.POST)
		if medicina.is_valid():
			medicina = medicina.save()
			return redirect('index_medicinas')
	else:
		medicina = FormMedicina()
		context = {'medicinas':allmedicinas,
					'form':medicina}
	return render(request,'farmacos/index_medicinas.html',context)

def editar_medicina(request, pk):
	medicina = get_object_or_404(Medicina,pk=pk)
	template = 'farmacos/Registrar.html'
	if request.method == 'POST':
		form = FormMedicina(request.POST, instance=medicina)
		if form.is_valid():
			medicina = form.save()
			return redirect('index_medicinas')
	else:
		form = FormMedicina(instance = medicina)
	context = {'form':form}
	return render(request, template, context)

def eliminar_medicina(request, pk):
	medicina = get_object_or_404(Medicina,pk=pk)
	medicina.delete()
	return redirect('index_medicinas')

def visualizar_medicina(request, pk):
	medicina = get_object_or_404(Medicina,pk=pk)
	template = 'farmacos/visualizacion.html'
	ficha_medicina = FichaMedicina.objects.filter(medicina=medicina.pk)
	context = {'medicina':medicina,
			'ficha_medicina':ficha_medicina}
	return render(request, template, context)


def index_vitaminas(request):
	allvitaminas = Vitamina.objects.all()
	if request.method == 'POST':
		vitamina = FormVitamina(request.POST)
		if vitamina.is_valid():
			vitamina = vitamina.save()
			return redirect('index_vitaminas')
	else:
		vitamina = FormVitamina()
		context = {'vitaminas':allvitaminas,
					'form':vitamina}
	return render(request,'farmacos/index_vitaminas.html',context)


def editar_vitamina(request,pk):
	vitamina = get_object_or_404(Vitamina,pk=pk)
	template = 'farmacos/Registrar.html'
	if request.method == 'POST':
		form = FormVitamina(request.POST, instance=vitamina)
		if form.is_valid():
			vitamina = form.save()
			return redirect('index_vitaminas')
	else:
		form = FormVitamina(instance = vitamina)
	context = {'form':form}
	return render(request, template, context)

def eliminar_vitamina(request,pk):
	vitamina = get_object_or_404(Vitamina,pk=pk)
	vitamina.delete()
	return redirect('index_vitaminas')

def visualizar_vitamina(request,pk):
	vitamina = get_object_or_404(Vitamina,pk=pk)
	template = 'farmacos/visualizacion.html'
	ficha_vitamina = FichaVitamina.objects.filter(vitamina=vitamina.pk)
	context = {'vitamina':vitamina,
			'ficha_vitamina':ficha_vitamina}
	return render(request, template, context)


def index_vacunas(request):
	allvacunas = Vacuna.objects.all()
	if request.method == 'POST':
		vacuna = FormVacuna(request.POST)
		if vacuna.is_valid():
			vacuna = vacuna.save()
			return redirect('index_vacunas')
	else:
		vacuna = FormVacuna()
		context = {'vacunas':allvacunas,
					'form':vacuna}
	return render(request,'farmacos/index_vacunas.html',context)


def editar_vacuna(request,pk):
	vacuna = get_object_or_404(Vacuna,pk=pk)
	template = 'farmacos/Registrar.html'
	if request.method == 'POST':
		form = FormVacuna(request.POST, instance=vacuna)
		if form.is_valid():
			vacuna = form.save()
			return redirect('index_vacunas')
	else:
		form = FormVacuna(instance = vacuna)
	context = {'form':form}
	return render(request, template, context)

def eliminar_vacuna(request,pk):
	vacuna = get_object_or_404(Vacuna,pk=pk)
	vacuna.delete()
	return redirect('index_vacunas')

def visualizar_vacuna(request,pk):
	vacuna = get_object_or_404(Vacuna,pk=pk)
	template = 'farmacos/visualizacion.html'
	ficha_vacuna = FichaVacuna.objects.filter(vacuna=vacuna.pk)
	context = {'vacuna':vacuna,
			'ficha_vacuna':ficha_vacuna}
	return render(request, template, context)
##################################################

def index_ficha_medicina(request):
	allficha_medicina = FichaMedicina.objects.all()
	if request.method == 'POST':
		ficha_medicina = FormFichaMedicina(request.POST)
		if ficha_medicina.is_valid():
			ficha_medicina = ficha_medicina.save()
			return redirect('index_ficha_medicina')
	else:
		ficha_medicina = FormFichaMedicina()
		context = {'ficha_medicina':allficha_medicina,
					'form':ficha_medicina}
	return render(request,'fichas/index_ficha_medicina.html',context)

def editar_ficha_medicina(request, pk):
	ficha_medicina = get_object_or_404(FichaMedicina,pk=pk)
	template = 'farmacos/Registrar.html'
	if request.method == 'POST':
		form = FormFichaMedicina(request.POST, instance=ficha_medicina)
		if form.is_valid():
			ficha_medicina = form.save()
			return redirect('index_ficha_medicina')
	else:
		form = FormFichaMedicina(instance = ficha_medicina)
	context = {'form':form}
	return render(request, template, context)

def eliminar_ficha_medicina(request, pk):
	ficha_medicina = get_object_or_404(FichaMedicina,pk=pk)
	ficha_medicina.delete()
	return redirect('index_ficha_medicinas')

def visualizar_ficha_medicina(request, pk):
	ficha_medicina = get_object_or_404(FichaMedicina,pk=pk)
	template = 'farmacos/visualizacion.html'
	#ficha_medicina = FichaMedicina.objects.filter(medicina=medicina.pk)
	context = {'ficha_medicina':ficha_medicina}
	return render(request, template, context)


def index_ficha_vitamina(request):
	allficha_vitaminas = FichaVitamina.objects.all()
	if request.method == 'POST':
		ficha_vitamina = FormFichaVitamina(request.POST)
		if ficha_vitamina.is_valid():
			ficha_vitamina = ficha_vitamina.save()
			return redirect('index_ficha_vitamina')
	else:
		ficha_vitamina = FormFichaVitamina()
		context = {'ficha_vitamina':allficha_vitaminas,
					'form':ficha_vitamina}
	return render(request,'fichas/index_ficha_vitamina.html',context)


def editar_ficha_vitamina(request,pk):
	ficha_vitamina = get_object_or_404(FichaVitamina,pk=pk)
	template = 'farmacos/Registrar.html'
	if request.method == 'POST':
		form = FormFichaVitamina(request.POST, instance=ficha_vitamina)
		if form.is_valid():
			ficha_vitamina = form.save()
			return redirect('index_ficha_vitamina')
	else:
		form = FormFichaVitamina(instance = ficha_vitamina)
	context = {'form':form}
	return render(request, template, context)

def eliminar_ficha_vitamina(request,pk):
	ficha_vitamina = get_object_or_404(FichaVitamina,pk=pk)
	ficha_vitamina.delete()
	return redirect('index_ficha_vitamina')

def visualizar_ficha_vitamina(request,pk):
	ficha_vitamina = get_object_or_404(FichaVitamina,pk=pk)
	template = 'farmacos/visualizacion.html'
	#ficha_vitamina = FichaVitamina.objects.filter(vitamina=vitamina.pk)
	#context = {'vitamina':vitamina,
	context = {'ficha_vitamina':ficha_vitamina}
	return render(request, template, context)


def index_ficha_vacuna(request):
	allficha_vacunas = FichaVacuna.objects.all()
	if request.method == 'POST':
		ficha_vacuna = FormFichaVacuna(request.POST)
		if ficha_vacuna.is_valid():
			ficha_vacuna = ficha_vacuna.save()
			return redirect('index_ficha_vacuna')
	else:
		ficha_vacuna = FormFichaVacuna()
		context = {'ficha_vacuna':allficha_vacunas,
					'form':ficha_vacuna}
	return render(request,'fichas/index_ficha_vacuna.html',context)


def editar_ficha_vacuna(request,pk):
	ficha_vacuna = get_object_or_404(FichaVacuna,pk=pk)
	template = 'farmacos/Registrar.html'
	if request.method == 'POST':
		form = FormFichaVacuna(request.POST, instance=ficha_vacuna)
		if form.is_valid():
			ficha_vacuna = form.save()
			return redirect('index_ficha_vacuna')
	else:
		form = FormFichaVacuna(instance = ficha_vacuna)
	context = {'form':form}
	return render(request, template, context)

def eliminar_ficha_vacuna(request,pk):
	ficha_vacuna = get_object_or_404(FichaVacuna,pk=pk)
	ficha_vacuna.delete()
	return redirect('index_ficha_vacuna')

def visualizar_ficha_vacuna(request,pk):
	ficha_vacuna = get_object_or_404(FichaVacuna,pk=pk)
	template = 'farmacos/visualizacion.html'
	#ficha_vacuna = FichaVacuna.objects.filter(vacuna=vacuna.pk)
	#context = {'vacuna':vacuna,
	context = {'ficha_vacuna':ficha_vacuna}
	return render(request, template, context)

##################################################
def RegistrarVacuna(request):
    template = 'farmacos/Registrar.html'
    if request.method == 'POST':
        farmaco = FormVacuna(request.POST)
        if farmaco.is_valid():
            farmaco.save()
            return redirect('index_vacunas')
    else:
        farmaco = FormVacuna()
        context = {'form':farmaco}
    return render(request,template,context)
    
def RegistrarVitamina(request):
    template = 'farmacos/Registrar.html'
    if request.method == 'POST':
        farmaco = FormVitamina(request.POST)
        if farmaco.is_valid():
            farmaco.save()
            return redirect('index_vitaminas')
    else:
        farmaco = FormVitamina()
        context = {'form':farmaco}
    return render(request,template,context)
    
def RegistrarMedicina(request):
    template = 'farmacos/Registrar.html'
    if request.method == 'POST':
        farmaco = FormMedicina(request.POST)
        if farmaco.is_valid():
            farmaco.save()
            return redirect('index_medicinas')
    else:
        farmaco = FormMedicina()
        context = {'form':farmaco}
    return render(request,template,context)
""" 
def RegistrarFVet(request):
    template = 'farmacos/Registrar.html'
    if request.method == 'POST':
        farmaco = FormFichaVet(request.POST)
        if farmaco.is_valid():
            farmaco.save()
            return redirect('index_ficha')
    else:
        farmaco = FormFichaVet()
        context = {'form':farmaco}
    return render(request,template,context)
"""     
def RegistrarFMedicina(request):
    template = 'farmacos/Registrar.html'
    if request.method == 'POST':
        farmaco = FormFichaMedicina(request.POST)
        if farmaco.is_valid():
            farmaco.save()
            return redirect('index_ficha_medicinas')
    else:
        farmaco = FormFichaMedicina()
        context = {'form':farmaco}
    return render(request,template,context)
    
def RegistrarFVitamina(request):
    template = 'farmacos/Registrar.html'
    if request.method == 'POST':
        farmaco = FormFichaVitamina(request.POST)
        if farmaco.is_valid():
            farmaco.save()
            return redirect('index_ficha_vitaminas')
    else:
        farmaco = FormFichaVitamina()
        context = {'form':farmaco}
    return render(request,template,context)
    
def RegistrarFVacuna(request):
    template = 'farmacos/Registrar.html'
    if request.method == 'POST':
        farmaco = FormFichaVacuna(request.POST)
        if farmaco.is_valid():
            farmaco.save()
            return redirect('index_ficha_vacunas')
    else:
        farmaco = FormFichaVacuna()
        context = {'form':farmaco}
    return render(request,template,context)
    


