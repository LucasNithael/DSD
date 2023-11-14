from suds.client import Client

# URL do WSDL do serviço web SOAP
url = 'http://localhost:8000/?wsdl'

# Criação do cliente SOAP
client = Client(url)

# Exemplo de chamada do método listar_alunos do serviço web SOAP
try:
    result = client.service.cadastrar_aluno('lucas', 6, 6)
    print(f"Resultado da listagem de alunos: {result}")
except Exception as e:
    print(f"Erro ao chamar o serviço: {e}")
