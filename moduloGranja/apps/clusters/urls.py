from django.urls import path, include
from apps.clusters.views import index_clusters
from . import views

urlpatterns = [
    path('', index_clusters,name = 'index_cluster'),
    path('tablacluster/<int:pk>/',views.tablacluster,name = 'tablacluster'),
    path('asignar/<int:pk>/<int:status>/',views.asignarPersonal,name="asignarPersonal"),
    path('removePersonalC/<int:pkC>/<int:pkP>/',views.removerPersonal,name='removerPersonal'),
    path('insertPersonalC/<int:pkC>/<int:pkP>/',views.insertPersonal,name='insertPersonal'),
    path('removeCerdoC/<int:pkC>/<int:pkc>/',views.removeCerdo,name='removeCerdoC'),
    path('insertCerdoC/<int:pkC>/<int:pkc>/',views.insertCerdo,name='insertCerdoC'),
]
