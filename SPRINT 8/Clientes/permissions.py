from rest_framework import permissions
from .models import Cliente

class IsOwnerAndAuthenticated(permissions.BasePermission):
  def has_permission(self, request, view):
    return request.user.is_authenticated

  def has_object_permission(self, request, view, obj):
    return obj == request.user.customer_id
  
class IsOwnerOrAdmin(permissions.BasePermission):
  def has_permission(self, request, view):
    return request.user.is_authenticated or request.user.is_staff

  def has_object_permission(self, request, view, obj):
    if request.user.is_staff:
      return True
    cliente = Cliente.objects.get(customer_id=request.user.customer_id.customer_id)
    return obj == cliente.address_id