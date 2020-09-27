from django import forms
from bootstrap_datepicker_plus import DatePickerInput
from .models import (
			Vacuna,Vitamina,Medicina,
			FichaMedicina,FichaVitamina,FichaVacuna,FichaVet
)

class FormVacuna(forms.ModelForm):
	class Meta:
		model = Vacuna
		fields = ['nombre_vacuna','marca','fecha_vencimiento']
		widgets = {'fecha_vencimiento': DatePickerInput(format='%m/%d/%Y'),}

class FormVitamina(forms.ModelForm):
	class Meta:
		model = Vitamina
		fields = ['nombre_vit','marca','fecha_vencimiento']
		widgets = {'fecha_vencimiento': DatePickerInput(format='%m/%d/%Y'),}

class FormMedicina(forms.ModelForm):
	class Meta:
		model = Medicina
		fields = ['nombre_med','marca','fecha_vencimiento']
		widgets = {'fecha_vencimiento': DatePickerInput(format='%m/%d/%Y'),}
"""
class FormFichaVet(forms.ModelForm):
	class Meta:
		model = FichaVet
		fields = ['nombre_fichavet','dias_tratamiento','frecuencia_xdia',
				'dosis_xtoma','fecha_inicio','cerdo']
"""
class FormFichaMedicina(forms.ModelForm):
	class Meta:
		model = FichaMedicina
		fields = ['nombre_fichavet',
				'dias_tratamiento',
				'frecuencia_xdia',
				'dosis_xtoma',
				'fecha_inicio',
				'cerdo',
				'medicina']
		labels = {'nombre_fichavet':'nombre\nficha',
				'dias_tratamiento': 'dias\ntratamiento',
				'frecuencia_xdia': 'frecuencia\npor dia',
				'dosis_xtoma': 'dosis\npor toma',
				'fecha_inicio': 'fecha\ninicio',
				'cerdo': 'cerdo',
				'medicina': 'medicina'}
		widgets = {'fecha_inicio': DatePickerInput(format='%m/%d/%Y'),}

class FormFichaVitamina(forms.ModelForm):
	class Meta:
		model = FichaVitamina
		fields = ['nombre_fichavet',
				'dias_tratamiento',
				'frecuencia_xdia',
				'dosis_xtoma',
				'fecha_inicio',
				'cerdo',
				'vitamina']
		widgets = {'fecha_inicio': DatePickerInput(format='%m/%d/%Y'),}

class FormFichaVacuna(forms.ModelForm):
	class Meta:
		model = FichaVacuna
		fields = ['nombre_fichavet',
				'dias_tratamiento',
				'frecuencia_xdia',
				'dosis_xtoma',
				'fecha_inicio',
				'cerdo',
				'vacuna']
		widgets = {'fecha_inicio': DatePickerInput(format='%m/%d/%Y'),}
