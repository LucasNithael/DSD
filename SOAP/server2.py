from spyne import Application, rpc, ServiceBase
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class Converter(ServiceBase):

    @rpc(float, _returns=float)
    def celsius_to_fahrenheit(ctx, celsius):
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit
    
    @rpc(float, _returns=float)
    def fahrenheit_to_kelvin(ctx, fahrenheit):
        kelvin = (fahrenheit - 32) * 5/9 + 273.15
        return kelvin
    
    @rpc(float, _returns=float)
    def fahrenheit_to_celsius(ctx, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        return celsius
    

    @rpc(float, _returns=float)
    def kelvin_para_celsius(ctx, kelvin):
        celsius = kelvin - 273.15
        return celsius



application = Application([Converter], 'converter',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())



wsgi_application = WsgiApplication(application)
server = make_server('localhost', 8000, wsgi_application)
print("Servidor SOAP iniciado. Aguardando requisições...")
server.serve_forever()

