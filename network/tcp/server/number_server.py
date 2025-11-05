import socket
import time

HOST = ''
PORT = 9997

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"[Number Server] Listening on port {PORT}...")

while True:
    client_socket, addr = server_socket.accept()
    print(f"[Client Connected] {addr}")
    
    for i in range(1, 11):
        msg = str(i)
        client_socket.sendall(msg.encode('utf-8'))
        time.sleep(0.5)
    
    client_socket.close()
