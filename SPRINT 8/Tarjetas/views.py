from rest_framework import generics, exceptions
from .models import Tarjeta
from .serializers import TarjetaSerializer
from .permissions import IsAuthenticatedAndAdmin

# Create your views here.
class TarjetaListView(generics.ListAPIView):
  permission_classes = [IsAuthenticatedAndAdmin]
  serializer_class = TarjetaSerializer

  def get_queryset(self):
    id = self.kwargs['pk']
    tarjetas = Tarjeta.objects.filter(customer_id = id, tipo_tarjeta = "crédito")
    
    if not tarjetas.exists():
      raise exceptions.NotFound(detail="No encontrado.")

    return tarjetas