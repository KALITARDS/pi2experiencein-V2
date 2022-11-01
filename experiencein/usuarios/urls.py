from django.urls import path
from usuarios.views import RegistrarUsuarioView

urlpatterns = [
 path('registrar/', RegistrarUsuarioView.as_view(), name='registrar')
]