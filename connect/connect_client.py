import socket
import sys
import json
import database

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

bool = True
while bool==True:
    username = input("Enter your username: ")
    if database.verify_username(username) == 1:
        password = input("Enter your password: ")
        if database.verify_password(password) == 1:
            bool = False
        else:
            print("Incorrect password. ")
            print("Try again. ")
    else:
        print("User not found. ")
        print("Do you want to create new account? 1 - YES / 2 - NO")
        choice = int(input())
        if choice == 1:
            password = input("Enter your password: ")
            database.create_user(username, password)
            bool = False



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