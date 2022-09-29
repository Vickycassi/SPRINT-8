from django.db import models
from Clientes.models import Cliente

# Create your models here.
class MarcasTarjeta(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.TextField()

    class Meta:
        managed = False
        db_table = 'marcas_tarjeta'

class Tarjeta(models.Model):
    numero = models.IntegerField(primary_key=True)
    cvv = models.IntegerField(db_column='CVV', blank=True, null=True)  # Field name made lowercase.
    fecha_otorgamiento = models.TextField(blank=True, null=True)
    fecha_expiracion = models.TextField(blank=True, null=True)
    tipo_tarjeta = models.TextField(blank=True, null=True)
    marca_tarjeta = models.ForeignKey(MarcasTarjeta, on_delete=models.DO_NOTHING,  db_column='marca_tarjeta')
    customer_id = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING, db_column='customer_id')

    class Meta:
        managed = False
        db_table = 'tarjeta'