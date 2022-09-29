from django.urls import path
from .views import PrestamosView, PrestamoListView, PrestamoCreateView, PrestamoDeleteView

urlpatterns = [
    path('api/prestamos/<int:pk>/', PrestamoListView.as_view()),
    path('api/prestamos/create/<int:pk>/<int:account_id>/', PrestamoCreateView.as_view({"post": "create"})),
    path('api/prestamos/delete/<int:pk>/<int:account_id>/', PrestamoDeleteView.as_view()),
    path('prestamos/', PrestamosView.as_view(), name = 'prestamos')
]