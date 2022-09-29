from django.db import models
from Clientes.models import Cliente

# Create your models here.
class TipoCuenta(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipo_cuenta'

class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING, db_column='customer_id')
    balance = models.IntegerField()
    iban = models.TextField()
    tipo_cuenta = models.ForeignKey(TipoCuenta, on_delete=models.DO_NOTHING, db_column='tipo_cuenta', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuenta'

class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField(db_column='employee_DNI')  # Field name made lowercase.
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'empleado'