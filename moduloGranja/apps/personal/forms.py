from django import forms
from bootstrap_datepicker_plus import DatePickerInput
from .models import Personal

class FormPersonal(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ['nombre_personal','dni','vencimiento_carnet']
        widgets = {
                'vencimiento_carnet': DatePickerInput(
                    format='%m/%d/%Y'),
                }
