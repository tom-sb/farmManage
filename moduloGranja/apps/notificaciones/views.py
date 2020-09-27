from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def noti_home(request):
	return render(request,'notificaciones/home.html')
