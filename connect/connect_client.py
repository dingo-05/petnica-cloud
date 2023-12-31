import socket
import sys
import json
import database
import headers
import menu
import buffer
import hashlib

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

salt = "Branimir"
bool = True

while bool==True:
    username = input("Enter your username: ")
    if database.verify_username(username) == 1:
        password = input("Enter your password: ")
        database_password = password + salt
        hashed_password = hashlib.md5(database_password.encode())
        hashed_password = hashed_password.hexdigest()
        if database.verify_password(hashed_password) == 1:
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
            database_password = password + salt
            hashed_password = hashlib.md5(database_password.encode())
            hashed_password = hashed_password.hexdigest()
            database.create_user(username, hashed_password)
            bool = False



    #if(username is in database):
    #    ask password
    #else:
    #    ask if you want to create account



sock.connect((SERVER_IP, SERVER_PORT))
try:
    conbuff = buffer.Buffer(sock)
    while bool==True:
        username = input("Enter your username: ")
        conbuff.put_utf8(username)
        userTrue = conbuff.get_utf8()
        if username == 1:
            password = input("Enter your password: ")
            database_password = password + salt
            hashed_password = hashlib.md5(database_password.encode())
            hashed_password = hashed_password.hexdigest()
            conbuff.put_utf8(hashed_password)
            passGood = conbuff.get_utf8()
            if passGood == 1:
                bool = False
            else:
                print("Incorrect password. ")
                print("Try again. ")
        else:
            print("User not found. ")
            print("Do you want to create new account? 1 - YES / 2 - NO")
            choice = int(input())
            conbuff.put_utf8(choice)
            if choice == 1:
                password = input("Enter your password: ")
                database_password = password + salt
                hashed_password = hashlib.md5(database_password.encode())
                hashed_password = hashed_password.hexdigest()
                conbuff.put_utf8(hashed_password)
                database.create_user(username, hashed_password)
                bool = False
    while True:
        msg = input("Enter command: ")#change later with location in files
        menu.openMenu(msg,sock)
        print("Menu Closed")
except KeyboardInterrupt:
    sock.close()
    exit()