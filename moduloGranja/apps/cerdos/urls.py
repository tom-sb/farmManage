from django.urls import path
from . import views

urlpatterns = [
    path('',views.index_cerdos,name='index_cerdos'),
    path('registrarCerdo',views.registrarCerdo,name='registrarCerdo'),
    path('registrarRaza',views.registrarRaza,name='registrarRaza'),
    path('eliminarCerdo',views.eliminarCerdo,name='eliminarCerdo'),
    path('determinarGalpon/<int:pk>',views.determinarGalpon,name='determinarGalpon'),
    path('engorde/',views.index_engorde,name='index_engorde'),    
    path('informeCerdo/<slug:pk>/',views.visualizarCerdo,name='visualizarCerdo'),
    path('registrar/<slug:pk>',views.RegistrarReproductor,name="RegistrarRep"),
]
#path('eliminarCerdo/<slug:pk>/',views.eliminarCerdo,name='eliminarCerdo'),
