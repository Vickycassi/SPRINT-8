from django.db import models

# Create your models here.
class Direccion(models.Model):
    address_id = models.AutoField(primary_key=True)
    ciudad = models.TextField()
    pais = models.TextField()
    provincia = models.TextField()
    calle = models.TextField()

    class Meta:
        managed = True
        db_table = 'direccion'

class TipoCliente(models.Model):
    tipo = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipo_cliente'

class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()
    customer_dni = models.TextField(db_column='customer_DNI')  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()
    tipo_cliente = models.ForeignKey(TipoCliente, on_delete=models.DO_NOTHING, db_column='tipo_cliente')
    address_id = models.ForeignKey(Direccion, on_delete=models.DO_NOTHING, db_column='address_id')

    class Meta:
        managed = False
        db_table = 'cliente'