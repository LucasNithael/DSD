from spyne import Application, rpc, ServiceBase
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server
from flask_cors import CORS


class Converter(ServiceBase):
    @rpc(float, _returns=float)
    def celsius_to_fahrenheit(ctx, celsius):
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit
    
    @rpc(float, _returns=float)
    def celsius_to_kelvin(ctx, celsius):
        kelvin = celsius + 273.15
        return kelvin

    @rpc(float, _returns=float)
    def fahrenheit_to_celsius(ctx, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        return celsius
    
    @rpc(float, _returns=float)
    def fahrenheit_to_kelvin(ctx, fahrenheit):
        kelvin = (fahrenheit - 273.15) * 9/5 + 32
        return kelvin
    
    @rpc(float, _returns=float)
    def kelvin_para_fahrenheitx(ctx, kelvin):
        fahrenheit = (kelvin - 273.15) * 9/5 + 32
        return fahrenheit
    
    @rpc(float, _returns=float)
    def kelvin_para_celsius(ctx, kelvin):
        celsius = kelvin - 273.15
        return celsius


application = Application([Converter], 'converter',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())


# Função que lida com as solicitações SOAP e adiciona cabeçalhos CORS manualmente
def handle_request(environ, start_response):
    # Adicione cabeçalhos CORS aqui, se necessário
    headers = [
        ('Content-type', 'text/xml'),
        ('Access-Control-Allow-Origin', '*'),  # Configurar para permitir todos os origens
        ('Access-Control-Allow-Methods', 'POST, OPTIONS'),
        ('Access-Control-Allow-Headers', 'Content-Type, SOAPAction'),
    ]

    # Chame o manipulador WsgiApplication com cabeçalhos CORS adicionados
    return WsgiApplication(application)(environ, start_response, headers=headers)

# Configurar o servidor WSGI com a função personalizada que lida com CORS
server = make_server('0.0.0.0', 8000, handle_request)
print("Servidor SOAP iniciado. Aguardando requisições...")
server.serve_forever()
