import socket

HOST = ''
PORT = 9998

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"[Echo Server] Listening on port {PORT}...")

while True:
    client_socket, addr = server_socket.accept()
    print(f"[Client Connected] {addr}")
    
    data = client_socket.recv(1024)
    if not data:
        break
    print("받은 데이터:", data.decode('utf-8'))
    client_socket.sendall(data)
    
    client_socket.close()
