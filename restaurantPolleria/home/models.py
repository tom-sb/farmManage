from django.db import models

# Create your models here.

factura ='facturas/'

class Factura(models.Model):
    nroFac1 = models.CharField(max_length=100) #vector[2]
    nroFac2 = models.CharField(max_length=100) #vector[3]
    fecha =  models.CharField(max_length=100) #vector[4]
    RUC = models.CharField(max_length=100) #vector[5]
    extra = models.CharField(max_length=100)#vector[1]
    rucEmpresa = models.CharField(max_length=100) #vector[0]
    def __str__(self):
        return self.getNrFactura()
    def consultar(self):
        #cons
        a=1

    def getNrFactura(self):
        return self.nroFac1+'-'+self.nroFac2

    def getFecha(self):
        return self.fecha

    def getRUC(self):
        return self.RUC

    def getdirPDF(self):
        return factura + self.getNrFactura()+'.pdf'
    
    def getXML(self):
        return factura + self.rucEmpresa+'-'+self.extra+'-'+self.getNrFactura()+'.zip'

