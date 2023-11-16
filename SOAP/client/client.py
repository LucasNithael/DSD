from suds.client import Client

# URL do WSDL do serviço web SOAP
url = 'http://localhost:8000/?wsdl'

# Criação do cliente SOAP
client = Client(url)

# Exemplo de chamada do método cadastrar_aluno do serviço web SOAP
try:
    result = client.service.celsius_para_fahrenheit(32)
    print(f"O resultado é: {result}")
except Exception as e:
    print(f"Erro ao chamar o serviço: {e}")
