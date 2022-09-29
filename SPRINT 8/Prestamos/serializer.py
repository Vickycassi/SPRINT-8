from rest_framework import serializers
from .models import Prestamo

class PrestamoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Prestamo
    fields = ('loan_total', 'loan_type')
    read_only_fields = ('loan_id', )

class PrestamoCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Prestamo
    fields = '__all__'
    read_only_fields = ('loan_id', 'customer_id')