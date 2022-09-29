from .permissions import IsAuthenticated
from .serializers import CuentaSerializer
from .models import Cuenta
from rest_framework import generics, exceptions

# Create your views here.
class CuentaListView(generics.ListAPIView):
  permission_classes = [IsAuthenticated]
  serializer_class = CuentaSerializer

  def get_queryset(self):
    id = self.kwargs['pk']
    user_id = self.request.user.customer_id.customer_id
    cuentas = Cuenta.objects.filter(customer_id = id)

    if not cuentas.exists():
      raise exceptions.NotFound(detail="No encontrado.")
    if user_id != id:
      raise exceptions.PermissionDenied(detail="Usted no tiene permiso para realizar esta acción.")

    return cuentas