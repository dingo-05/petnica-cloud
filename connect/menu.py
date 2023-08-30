import socket
import os
import headers
import buffer
import json


def openMenu(text,sock):
    global sock_global
    sock_global= sock
    if '&' in text:
        print('Command has unauthorized characters!')
        return()
    command = text.split(" ",1)[0]
    if(command == 'upload'):
        return upload(text.split(" ")[1])
    elif(command == 'download'):
        return download(text.split(" ")[1])
    elif(command == 'mkdir'):
        return makeDIR(text.split(" ")[1])
    elif(command == 'cd'):
        return changeDIR(text.split(" ")[1])
    elif(command == 'rm'):
        return remove_item(text.split(" ", 1)[1])
    elif(command == 'help'):
        print('There are folowing commands:\nupload - uploads file from the server\ndownload - downloads file from the server\nmkdir - create a new directory\ncd - change directory\nxrm - remove item\nhelp - help with commands')
        return ()
    print('type help command for help')
    return ()
    
def upload(file_name):
    
    sbuf = buffer.Buffer(sock_global)
    
    
    command = 'upload'
    print(file_name)
    
    
    sbuf.put_utf8(command)
    sbuf.put_utf8(file_name)
    file_size = os.path.getsize(file_name)
    sbuf.put_utf8(str(file_size))
    if not os.path.isfile(file_name):
        print("File not found")
        return()
    with open(file_name, 'rb') as f:
            sbuf.put_bytes(f.read())
    print('File Sent')
    
    

def download(file_name):
    sbuf = buffer.Buffer(sock_global)
    
    command = 'download'
    sbuf.put_utf8(command)
    print('Downloading:',file_name)
    sbuf.put_utf8(file_name)
    found=sbuf.get_utf8()
    if found == 'File not found':
        print('File not found')
        return()
    file_size = int(sbuf.get_utf8())
    with open(file_name, 'wb') as f:
            remaining = file_size
            while remaining:
                chunk_size = 4096 if remaining >= 4096 else remaining
                chunk = sbuf.get_bytes(chunk_size)
                if not chunk: break
                f.write(chunk)
                remaining -= len(chunk)
            if remaining:
                print('File incomplete.  Missing',remaining,'bytes.')
            else:
                print('File received successfully.')
    
    
    
def makeDIR(dir_name):
    sbuf = buffer.Buffer(sock_global)
    command = 'mkdir'
    sbuf.put_utf8(command)
    sbuf.put_utf8(dir_name)
    message=sbuf.get_utf8()
    print(message)
def changeDIR(dir_name):
    sbuf = buffer.Buffer(sock_global)
    command = 'cd'
    sbuf.put_utf8(command)
    sbuf.put_utf8(dir_name)
    message=sbuf.get_utf8()
    print(message)
def remove_item(item_name):
    sbuf = buffer.Buffer(sock_global)
    command_parts = item_name.split()
    command = 'rm'
    
    if len(command_parts) == 0:
        print("No item specified for removal.")
        return
    if '\\' in item_name or '/' in item_name:
        print("Can't delete that directory.")
        return

    item = command_parts[-1]  
    
    if item == '*':
        confirm = input("Are you sure you want to delete all folders in the current directory? (yes/no): ")
        if confirm.lower() == "yes":
            sbuf.put_utf8(command)
            sbuf.put_utf8(item)
            message = sbuf.get_utf8()  
        else:
            message = "Operation canceled."
    else:
        sbuf.put_utf8(command)
        sbuf.put_utf8(item)
        message = sbuf.get_utf8()  
    
    print(message)
