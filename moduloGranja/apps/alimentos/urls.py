from django.urls import path
from apps.alimentos.views import index_alimentos, ficha_alimento
from . import views

urlpatterns = [
    path('',views.index_alimentos,name='index_alimentos'),
	path('editar/<int:pk>',views.editarAlimento,name='editarAlimento'),
	path('eliminar/<int:pk>',views.eliminarAlimento,name='eliminarAlimento'),
	path('visualizar/<int:pk>',views.visualizarAlimento,name='visualizarAlimento'),
	path('ficha_alimento/',views.ficha_alimento,name='ficha_alimento'),
	path('ficha_alimento_editar/<int:pk>',views.ficha_alimento_editar,name='ficha_alimento_editar'),
	path('ficha_alimento_eliminar/<int:pk>',views.ficha_alimento_eliminar,name='ficha_alimento_eliminar'),
	path('ficha_alimento_visualizar/<int:pk>',views.ficha_alimento_visualizar,name='ficha_alimento_visualizar'),
]
