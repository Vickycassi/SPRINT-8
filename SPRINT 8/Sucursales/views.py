from rest_framework import generics, exceptions
from .serializers import SucursalSerializer
from .models import Sucursal
from .serializers import  SucursalPrestamoSerializer
from .permissions import IsAuthenticatedAndAdmin
from Clientes.models import Cliente
from Prestamos.models import Prestamo

# Create your views here.
class SucursalListView(generics.ListAPIView):
  serializer_class = SucursalSerializer
  queryset = Sucursal.objects.all()

class SucursalPrestamosListView(generics.ListAPIView):
  serializer_class = SucursalPrestamoSerializer
  permission_classes = [IsAuthenticatedAndAdmin]

  def get_queryset(self):
    id = self.kwargs['pk']
    clientes = Cliente.objects.filter(branch_id = id)
    prestamos = Prestamo.objects.filter(customer_id__in = clientes)

    if not clientes.exists():
      raise exceptions.NotFound(detail="No encontrado.")

    return prestamos