import socket
import sys

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
    while True:
        msg = input("Enter your message: ")
        msg = f"[{username}]: {msg}"
#        msg = headers.appendHeaders(msg)
        sock.send(msg)

#        try:
#            msgSize = int.from_bytes(receiveMessage(sock, headers.HEADER_LEN))
#            msg = b''
#            while len(msg) < msgSize:
#                msg += receiveMessage(sock, msgSize - len(msg))
#            msg = msg.decode()
#
#        except Exception as e:
#            print(f"Error: {e}")
#            break
#
#        print(msg)
except KeyboardInterrupt:
    sock.close()
    exit()