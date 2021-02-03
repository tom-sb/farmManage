from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def registro(request):
    data = {
        'form':CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            #autenticar
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Registro completado")
            #redirigir al home
            return redirect(to="/home")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)
