import socket
import sys
import headers
import menu
import buffer

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <ip> ")
    sys.exit(1)
    
SERVER_IP = sys.argv[1]
SERVER_PORT = int(1945)

def receiveMessage(conn, length):
    msg = conn.recv(length)
    if not msg:
        raise Exception("Connection closed")
    return msg

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



username = input("Enter your username: ")
#if(username is in database):
#    ask password
#else:
#    ask if you want to create account


sock.connect((SERVER_IP, SERVER_PORT))
try:
    sbuff=buffer.Buffer(sock)
    sbuff.put_utf8(username)
    while True:
        msg = input("Enter command: ")#change later with location in files
        menu.openMenu(msg,sock)
        print("Menu Closed")
except KeyboardInterrupt:
    sock.close()
    exit()