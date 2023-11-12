from suds.client import Client

# URL do WSDL do serviço web SOAP
url = 'http://localhost:8000/?wsdl'

# Criação do cliente SOAP
client = Client(url, transport=tcp.TcpTransport())

# Exemplo de chamada de método do serviço web SOAP
result = client.service.add(5, 10)

# Exibição do resultado
print(f"Resultado da adição: {result}")
