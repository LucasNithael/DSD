# myproject/myapp/urls.py
from django.urls import path
from .views import soap_service

urlpatterns = [
    path('soap/', soap_service),
    # outras rotas...
]
