import socket
import sys
import threading
import headers
import os
import buffer
import menu_server


SERVER_IP = socket.gethostbyname(socket.gethostname())
SERVER_PORT = int(1945)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((SERVER_IP, SERVER_PORT))

def receiveMessage(conn, length):
    msg = conn.recv(length)
    if not msg:
        raise Exception("Connection closed")
    return msg

def handleConnection(conn, addr):
    connbuf = buffer.Buffer(conn)
    username=connbuf.get_utf8()
    default="d:\\database\\"
    home_path=default+username+'\\'
    path=home_path
    if not os.path.exists(path):
        os.makedirs(path)
    while True:
        print('Listening for user:',username)
        command = connbuf.get_utf8()
        path=menu_server.openMenu(command,connbuf,path,home_path)
        

    conn.close()
    print(f"Closed connection from {addr}")


def acceptConnections():
    server.listen()
    print(f"Listening on {SERVER_IP}:{SERVER_PORT}")
    while True:
        conn, addr = server.accept()
        print(f"New connection from {addr}")
        threading.Thread(target=handleConnection, args=(conn, addr)).start()

acceptConnections()