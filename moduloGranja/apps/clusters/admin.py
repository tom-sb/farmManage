from django.contrib import admin
from apps.clusters.models import Cluster,CerdoCluster
# Register your models here.
admin.site.register(Cluster)
admin.site.register(CerdoCluster)
