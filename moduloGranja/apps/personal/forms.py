from django import forms
from bootstrap_datepicker_plus import DatePickerInput
from .models import Personal

class FormPersonal(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ['nombre','dni','fecha_ingreso','fecha_salida']
        widgets = {
                'fecha_ingreso': DatePickerInput(
                    format='%m/%d/%Y'),
                'fecha_salida': DatePickerInput(
                    format='%m/%d/%Y'),
                }
