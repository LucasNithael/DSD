# myapp/views.py
from django.http import HttpResponse
from spyne.server.django import DjangoApplication
from .soap_service import application as soap_application

soap_service = DjangoApplication(soap_application)

def soap_handler(request):
    if request.method == 'POST':
        response = HttpResponse(content_type='text/xml')
        soap_service.__call__(request, response)
        return response
    else:
        return HttpResponse(status=405, content='Method Not Allowed')
