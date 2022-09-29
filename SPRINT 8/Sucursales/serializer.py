from rest_framework import serializers
from Prestamos.models import Prestamo
from .models import Sucursal
from Prestamos.models import Prestamo

class SucursalSerializer(serializers.ModelSerializer):
  class Meta:
    model = Sucursal
    fields = '__all__'
    read_only_fields = ('branch_id', )

class SucursalPrestamoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Prestamo
    fields = '__all__'
    read_only_fields = ('loan_id', )