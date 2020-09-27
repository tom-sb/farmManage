from django.urls import path
from apps.personal.views import index_personal
from . import views

urlpatterns = [
	path('',index_personal,name='index_personal'),
        path('editar/<int:pk>/',views.editar_personal,name='editarPersonal'),
        path('eliminar/<int:pk>/',views.eliminar_personal,name='eliminarPersonal'),
        path('visualizar/<int:pk>/',views.visualizarPersonal,name='visualizarPersonal'),
        path('asignar/<int:pk>/',views.asignarTareas,name='asignarTareas'),
        path('asignar/<int:pkP>/<int:pkC>/',views.asignarCluster,name='asignarCluster'),
]
