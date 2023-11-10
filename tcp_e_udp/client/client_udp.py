import socket

# Configuração do cliente UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Lógica do cliente
while True:
    message = input('Digite uma mensagem para o servidor (ou "exit" para sair): ')
    client_socket.sendto(message.encode(), ('localhost', 12345))  # Envia a mensagem ao servidor

    if message.lower() == 'exit':
        break

    data, addr = client_socket.recvfrom(1024)  # Recebe a resposta do servidor
    print(f'Resposta do servidor: {data.decode()}')

client_socket.close()  # Fecha o socket do cliente
