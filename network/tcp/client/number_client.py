import socket

SERVER_IP = '172.19.5.80'
PORT = 9997

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, PORT))

while True:
    data = client_socket.recv(1024)
    if not data:
        break
    print("서버로부터 수신:", data.decode('utf-8'))

client_socket.close()
