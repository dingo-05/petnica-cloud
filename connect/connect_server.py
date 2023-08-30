import socket
import sys
import threading
import headers
import os
import buffer
import menu_server
import database


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
bool = True
def handleConnection(conn, addr):
    connbuf = buffer.Buffer(conn)
    while bool==True:
        username=connbuf.get_utf8()
        if database.verify_username(username) == 1:
            connbuf.put_utf8('1')
            password = connbuf.get_utf8()
            passGood = database.verify_password(password)
            if passGood=='1':
                connbuf.put_utf8('1')
                break
            else:
                connbuf.put_utf8('0')
        else:
            connbuf.put_utf8('0')
            choice = connbuf.get_utf8()
            if(choice=='1'):
                password = connbuf.get_utf8()
                database.create_user(username,password)
                break
                
    
    default="d:\\database\\"
    home_path=default+username
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