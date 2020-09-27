from django.contrib import admin
from apps.farmacos.models import FichaVet, Vacuna, Vitamina, Medicina, FichaVacuna, FichaVitamina, FichaMedicina 
# Register your models here.

admin.site.register(Vacuna)
admin.site.register(Vitamina)
admin.site.register(Medicina)
admin.site.register(FichaVitamina)
admin.site.register(FichaVacuna)
admin.site.register(FichaMedicina)
