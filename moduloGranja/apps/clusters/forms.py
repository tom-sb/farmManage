from django import forms
from .models import Cluster

class FormCluster(forms.ModelForm):
    class Meta:
        model = Cluster
        fields = ['nombre_cluster','capacidad','nro_galpon']
