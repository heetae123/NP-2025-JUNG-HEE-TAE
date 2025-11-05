import socket

SERVER_IP = '172.19.5.80'  # 예: 192.168.0.10
PORT = 9999

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, PORT))

data = client_socket.recv(1024)
print("[서버 시간]", data.decode('utf-8'))

client_socket.close()
