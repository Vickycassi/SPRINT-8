from django.urls import path
from .views import SucursalListView, SucursalPrestamosListView

urlpatterns = [
  path('', SucursalListView.as_view()),
  path('prestamos/<int:pk>/', SucursalPrestamosListView.as_view())
]