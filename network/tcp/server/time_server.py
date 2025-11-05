import socket
import datetime

HOST = ''          # 모든 인터페이스
PORT = 9999        # 포트 번호

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"[Time Server] Listening on port {PORT}...")

while True:
    client_socket, addr = server_socket.accept()
    print(f"[Client Connected] {addr}")
    
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    client_socket.sendall(current_time.encode('utf-8'))
    
    client_socket.close()
