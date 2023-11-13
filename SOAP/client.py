from suds.client import Client

# URL do WSDL do serviço web SOAP
url = 'http://localhost:8000/?wsdl'

# Criação do cliente SOAP
client = Client(url)

# Exemplo de chamada de método do serviço web SOAP
result = client.service.add(5, 10)
result2 = client.service.mul(5, 10)

# Exibição do resultado
print(f"Resultado da adição: {result2}")



# Obtenha a instância do serviço
service = client.service

# Liste os métodos disponíveis
methods = [method for method in dir(service) if callable(getattr(service, method)) and not method.startswith("__")]


# Exibição dos métodos disponíveis
print("Métodos disponíveis:")
for method in methods:
    print(method)



operations = [op for op in client.wsdl.services[0].ports[0].methods.keys()]

# Exibição dos métodos disponíveis
print("Métodos disponíveis:")
for operation in operations:
    print(operation)









