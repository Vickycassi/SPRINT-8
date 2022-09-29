from rest_framework import serializers
from .models import Cliente, Direccion

class DireccionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Direccion
    fields = '__all__'
    read_only_fields = ('address_id', )

class ClienteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Cliente
    fields = '__all__'
    read_only_fields = ('customer_id', )