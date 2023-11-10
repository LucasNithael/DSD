import socket

# Configuração do servidor TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))  # Escolha o IP e a porta para o servidor
server_socket.listen(5)  # Número máximo de conexões pendentes

print('Aguardando conexões...')
client_socket, addr = server_socket.accept()  # Aguarda por uma conexão

print(f'Conexão estabelecida com {addr}')

# Lógica do servidor
while True:
    data = client_socket.recv(1024)  # Recebe dados do cliente
    if not data:
        break
    print(f'Dados recebidos do cliente: {data.decode()}')
    response = input('Resposta para o cliente: ')  # Obter resposta do usuário
    client_socket.sendall(response.encode())  # Envia a resposta de volta ao cliente

client_socket.close()  # Fecha o socket do cliente
server_socket.close()  # Fecha o socket do servidor
