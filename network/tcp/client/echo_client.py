import socket

SERVER_IP = '172.19.5.80'
PORT = 9998

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, PORT))

msg = input("메시지 입력: ")
client_socket.sendall(msg.encode('utf-8'))

data = client_socket.recv(1024)
print("서버로부터:", data.decode('utf-8'))

client_socket.close()
