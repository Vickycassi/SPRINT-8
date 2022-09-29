from django.urls import path
from .views import IndexView, ClienteRetrieveView, DireccionUpdateView

urlpatterns = [
    path('api/clientes/<int:customer_id>/', ClienteRetrieveView.as_view()),
    path('api/clientes/direccion/<int:pk>/', DireccionUpdateView.as_view()),
    path('', IndexView.as_view(), name = 'index')
]