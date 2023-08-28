import socket
import sys
import threading



SERVER_IP = socket.gethostbyname(socket.gethostname())
SERVER_PORT = int(1945)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((SERVER_IP, SERVER_PORT))




def acceptConnections():
    server.listen()
    print(f"Listening on {SERVER_IP}:{SERVER_PORT}")
    while True:
        conn, addr = server.accept()
        print(f"New connection from {addr}")
        #threading.Thread(target=handleConnection, args=(conn, addr)).start()

acceptConnections()