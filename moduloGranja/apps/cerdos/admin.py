from django.contrib import admin
from apps.cerdos.models import Cerdo,Raza, Reproductora, Reproductor, Nacido, Engorde 
# Register your models here.
admin.site.register(Raza)
admin.site.register(Cerdo)
admin.site.register(Reproductora)
admin.site.register(Reproductor)
admin.site.register(Nacido)
admin.site.register(Engorde)
