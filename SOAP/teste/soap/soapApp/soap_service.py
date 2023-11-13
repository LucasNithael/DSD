# myapp/soap_service.py
from spyne import Application, rpc, ServiceBase, Integer
from spyne.protocol.soap import Soap11

class CalculatorService(ServiceBase):
    @rpc(Integer, Integer, _returns=Integer)
    def add(ctx, a, b):
        return a + b
    
    @rpc(Integer, Integer, _returns=Integer)
    def mul(ctx, a, b):
        return a * b

application = Application([CalculatorService], 'calculator',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())
