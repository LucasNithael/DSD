from spyne import Application, rpc, ServiceBase
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from flask_cors import CORS
from flask import Flask, request

class CorsService(ServiceBase):
    pass

class Converter(CorsService):

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

app = Flask(__name__)
CORS(app)  

headers_sent = []

def start_response(status, response_headers, exc_info=None):
   """WSGI compliant start_response function."""
   if exc_info:
       try:
           if headers_sent:
               raise exc_info[0](exc_info[1]).with_traceback(exc_info[2])
       finally:
           exc_info = None
       return
   headers_sent[:] = [status, response_headers]


@app.route("/soap", methods=["POST"])
def soap_handler():
   return wsgi_application(request.environ, start_response)

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
