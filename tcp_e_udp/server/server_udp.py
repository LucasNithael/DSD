import socket

# Configuração do servidor UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12345))  # Escolha o IP e a porta para o servidor

print('Aguardando mensagens...')

# Lógica do servidor
while True:
    data, addr = server_socket.recvfrom(1024)  # Recebe dados do cliente
    print(f'Mensagem recebida do cliente {addr}: {data.decode()}')
    response = input('Resposta para o cliente: ')  # Obter resposta do usuário
    server_socket.sendto(response.encode(), addr)  # Envia a resposta de volta ao cliente
