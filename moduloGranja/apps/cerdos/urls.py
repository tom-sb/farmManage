from django.urls import path
from apps.cerdos.views import index_cerdos, index_reproductora
from . import views

urlpatterns = [
    path('',views.index_cerdos,name='index_cerdos'),
    path('reproductora/',index_reproductora,name='index_reproductora'),    
    path('nacido/',views.index_nacido,name='index_nacido'),    
    path('engorde/',views.index_engorde,name='index_engorde'),    
    path('reproductor/',views.index_reproductor,name='index_reproductor'),
    path('informeCerdo/<int:pk>/',views.visualizarCerdo,name='visualizarCerdo'),
    path('eliminarCerdo/<int:pk>/',views.eliminarCerdo,name='eliminarCerdo'),
    path('registrar/<int:pk>',views.RegistrarReproductor,name="RegistrarRep"),
]
