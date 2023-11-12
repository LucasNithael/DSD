from spyne import Application, rpc, ServiceBase, Integer
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class CalculatorService(ServiceBase):
    @rpc(Integer, Integer, _returns=Integer)
    def add(ctx, a, b):
        return a + b

# Criação da aplicação SOAP
application = Application([CalculatorService], 'calculator',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

# Configuração do servidor WSGI
wsgi_application = WsgiApplication(application)

# Configuração do servidor HTTP
server = make_server('0.0.0.0', 8000, wsgi_application)

print("Servidor SOAP iniciado. Aguardando requisições...")
server.serve_forever()
