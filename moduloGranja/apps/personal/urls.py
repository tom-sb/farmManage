from django.urls import path
from apps.personal.views import index_personal
from . import views

urlpatterns = [
	path('',index_personal,name='index_personal'),
        path('registrar',views.registrarPersonal,name='registrarPersonal'),
        path('editar/<int:pk>/',views.PersonalUpdateView.as_view(),name='editarPersonal'),
        path('eliminar/<int:pk>/',views.PersonalDeleteView.as_view(),name='eliminarPersonal'),
        path('eliminar',views.eliminar_personals,name='eliminarPersonals'),
        path('visualizar/<int:pk>/',views.visualizarPersonal,name='visualizarPersonal'),
        path('asignar/<int:pk>/',views.asignarCluster,name='asignarCluster'),
]
