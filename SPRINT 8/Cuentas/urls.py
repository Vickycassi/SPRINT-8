from django.urls import path
from .views import CuentaListView

urlpatterns = [
  path('<int:pk>/', CuentaListView.as_view())
]