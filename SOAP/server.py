from spyne import Application, rpc, ServiceBase
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server
from flask_cors import CORS



class CorsService(ServiceBase):
    origin = '*'

    def _on_method_return_object(ctx):
        ctx.transport.resp_headers['Access-Control-Allow-Origin'] = \
                                                ctx.descriptor.service_class.origin

    CorsService.event_manager.add_listener('method_return_object', 
                                                                _on_method_return_object)


class Converter(CorsService):

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


wsgi_application = WsgiApplication(application)

server = make_server('0.0.0.0', 8000, wsgi_application)
print("Servidor SOAP iniciado. Aguardando requisições...")
server.serve_forever()
