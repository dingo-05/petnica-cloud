import socket
import os
import headers
import buffer


def openMenu(text,sock):
    global sock_global
    sock_global= sock
    if '&' in text:
        print('Command has unauthorized characters!')
        return()
    command = text.split(" ",1)[0]
    if(command == 'upload'):
        print(text)
        return upload(text.split(" ")[1])
    if(command == 'download'):
        return download(text.split(" ")[1])
    if(command == 'mkdir'):
        return makeDIR(text.split(" ")[1])
    if(command == 'cd'):
        return changeDIR(text.split(" ")[1])
    if(command == 'help'):
        print('There are folowing commands:\nupload - uploads file from the server\ndownload - downloads file from the server\nmkdir - create a new directory\ncd - change directory\nhelp - help with commands')
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
    
    with open(file_name, 'rb') as f:
            sbuf.put_bytes(f.read())
    print('File Sent')
    
    

def download(file_name):
    file_name
def makeDIR(dir_name):
    sock_global.send(headers.appendHeaders('mkdir'))
    sock_global.send(headers.appendHeaders(dir_name))
def changeDIR(dir_name):
    sock_global.send(headers.appendHeaders('cd'))
    sock_global.send(headers.appendHeaders(dir_name))