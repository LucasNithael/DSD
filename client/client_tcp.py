import socket

# Configuração do cliente TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))  # IP e porta do servidor

# Lógica do cliente
while True:
    message = input('Digite uma mensagem para o servidor (ou "exit" para sair): ')
    client_socket.sendall(message.encode())  # Envia a mensagem ao servidor
    if message.lower() == 'exit':
        break
    data = client_socket.recv(1024)  # Recebe a resposta do servidor
    print(f'Resposta do servidor: {data.decode()}')

client_socket.close()  # Fecha o socket do cliente
