from django.urls import path, include
from apps.notificaciones.views import noti_home

urlpatterns = [
    path('', noti_home),
]
