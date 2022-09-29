from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from rest_framework import generics
from .permissions import IsOwnerAndAuthenticated, IsOwnerOrAdmin
from .serializers import ClienteSerializer, DireccionSerializer
from .models import Cliente
from django.shortcuts import get_object_or_404

# Create your views here.
class IndexView(LoginRequiredMixin, generic.TemplateView):
  template_name = 'Clientes/index.html'

class ClienteRetrieveView(generics.RetrieveAPIView):
  permission_classes = [IsOwnerAndAuthenticated]
  serializer_class = ClienteSerializer
  lookup_field = 'customer_id'
  queryset = Cliente.objects.all()

class DireccionUpdateView(generics.UpdateAPIView):
  permission_classes = [IsOwnerOrAdmin]
  serializer_class = DireccionSerializer

  def get_queryset(self):
    id = self.kwargs["pk"]
    cliente = get_object_or_404(Cliente, customer_id=id)

    return cliente.address_id

  def get_object(self):
    obj = self.get_queryset()
    self.check_object_permissions(self.request, obj)
    return obj
