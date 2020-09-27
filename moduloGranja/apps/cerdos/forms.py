from django import forms
from bootstrap_datepicker_plus import DatePickerInput

from .models import Cerdo, Reproductora, Engorde, Nacido, Reproductor 

class FormCerdo(forms.ModelForm):
    class Meta:
        model = Cerdo
        fields = ('nombre_cerdo','raza','fecha_nac','peso',)
        widgets = {
                'fecha_nac': DatePickerInput(
                    format='%m/%d/%Y'),
                }

class FormReproductora(forms.ModelForm):
    class Meta:
        model = Reproductora
        fields = ('nro_inseminaciones','nro_partos','fecha_gestacion','embarazo','riesgo',)

class FormEngorde(forms.ModelForm):
    class Meta:
        model = Engorde
        fields = ('apto','score',)

class FormReproductor(forms.ModelForm):
    class Meta:
        model = Reproductor
        fields = ('nro_muestras','nro_hijos',)

class FormNacido(forms.ModelForm):
    class Meta:
        model = Nacido
        fields = ('apto',)
