from django.urls import path
from .views import TarjetaListView

urlpatterns = [
    path('<int:pk>/', TarjetaListView.as_view()),
]