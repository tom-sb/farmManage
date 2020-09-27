from django import forms
from bootstrap_datepicker_plus import DatePickerInput
from .models import Alimento, FichaAlimento

class FormAlimento(forms.ModelForm):
    class Meta:
        model = Alimento
        fields = ['nombre_alimento','stock_alimento']

class FormFichaAlimento(forms.ModelForm):
    class Meta:
        model = FichaAlimento
        fields = ['nombre_ficha','alimento','cluster','fecha_expiracion','frecuencia_xdia','cantidad_xtoma','auto_renovar']
        widgets = {"fecha_expiracion":DatePickerInput(format='%m/%d/%Y'),}
