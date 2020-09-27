from django.urls import path
from apps.farmacos.views import index_medicinas, index_vitaminas, index_vacunas, index_ficha_medicina, index_ficha_vitamina, index_ficha_vacuna
from . import views

urlpatterns = [
		path('medicinas/',index_medicinas,name ='index_medicinas'),
		path('editar_medicina/<int:pk>', views.editar_medicina, name = 'editar_medicina'),
		path('eliminar_medicina/<int:pk>', views.eliminar_medicina, name = 'eliminar_medicina'),
		path('visualizar_medicina/<int:pk>', views.visualizar_medicina, name = 'visualizar_medicina'),
		path('vitaminas/',index_vitaminas,name ='index_vitaminas'),
		path('editar_vitamina/<int:pk>', views.editar_vitamina, name = 'editar_vitamina'),
		path('eliminar_vitamina/<int:pk>', views.eliminar_vitamina, name = 'eliminar_vitamina'),
		path('visualizar_vitamina/<int:pk>', views.visualizar_vitamina, name = 'visualizar_vitamina'),
		path('vacunas/',index_vacunas,name ='index_vacunas'),
		path('editar_vacuna/<int:pk>', views.editar_vacuna, name = 'editar_vacuna'),
		path('eliminar_vacuna/<int:pk>', views.eliminar_vacuna, name = 'eliminar_vacuna'),
		path('visualizar_vacuna/<int:pk>', views.visualizar_vacuna, name = 'visualizar_vacuna'),

		path('ficha_medicina/',index_ficha_medicina,name ='index_ficha_medicina'),
		path('editar_ficha_medicina/<int:pk>', views.editar_ficha_medicina, name = 'editar_ficha_medicina'),
		path('eliminar_ficha_medicina/<int:pk>', views.eliminar_ficha_medicina, name = 'eliminar_ficha_medicina'),
		path('visualizar_ficha_medicina/<int:pk>', views.visualizar_ficha_medicina, name = 'visualizar_ficha_medicina'),
		path('ficha_vitamina/',index_ficha_vitamina,name ='index_ficha_vitamina'),
		path('editar_ficha_vitamina/<int:pk>', views.editar_ficha_vitamina, name = 'editar_ficha_vitamina'),
		path('eliminar_ficha_vitamina/<int:pk>', views.eliminar_ficha_vitamina, name = 'eliminar_ficha_vitamina'),
		path('visualizar_ficha_vitamina/<int:pk>', views.visualizar_ficha_vitamina, name = 'visualizar_ficha_vitamina'),
		path('ficha_vacuna/',index_ficha_vacuna,name ='index_ficha_vacuna'),
		path('editar_ficha_vacuna/<int:pk>', views.editar_ficha_vacuna, name = 'editar_ficha_vacuna'),
		path('eliminar_ficha_vacuna/<int:pk>', views.eliminar_ficha_vacuna, name = 'eliminar_ficha_vacuna'),
		path('visualizar_ficha_vacuna/<int:pk>', views.visualizar_ficha_vacuna, name = 'visualizar_ficha_vacuna'),
        path('registrarVacuna',views.RegistrarVacuna,name='registrarVac'),
        path('registrarVitamina',views.RegistrarVitamina,name='registrarVit'),
        path('registrarMedicina',views.RegistrarMedicina,name='registrarMed'),
        #path('registrarFVet',views.RegistrarFVet,name='registrarFVet'),
        path('registrarFMedicina',views.RegistrarFMedicina,name='registrarFMed'),
        path('registrarFVitamina',views.RegistrarFVitamina,name='registrarFVit'),
        path('registrarFVacuna',views.RegistrarFVacuna,name='registrarFVac'),
]
