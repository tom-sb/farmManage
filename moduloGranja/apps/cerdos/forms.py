from django import forms
from bootstrap_datepicker_plus import DatePickerInput

from .models import Cerdo,Raza, Reproductora, Engorde, Nacido, Reproductor 

class FormRaza(forms.ModelForm):
    class Meta:
        model = Raza
        fields =['nombre','edad_ideal','peso_ideal']

class FormCerdo(forms.ModelForm):
    class Meta:
        model = Cerdo
        fields =['nombre','raza','genero','fecha_nacimiento','peso']
        widgets = {
                'fecha_nacimiento': DatePickerInput(
                    format='%m/%d/%Y')
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
