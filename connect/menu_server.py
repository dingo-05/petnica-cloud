import socket
import os
import headers
import buffer


def openMenu(command,con,path1,home_path1):
    global connbuf
    global path
    global home_path
    connbuf = con
    path=path1
    home_path=home_path1
    if(command == 'upload'):
        return upload()
    elif(command == 'download'):
        return download()
    elif(command == 'mkdir'):
        return makeDIR(text.split(" ")[1])
    elif(command == 'cd'):
        return changeDIR(text.split(" ")[1])
    print('Unknown command')
    return ()

def upload():
    file_name = connbuf.get_utf8()
    if '\\' in file_name:
        file_name = file_name.split('\\')[-1]
    print(file_name)
    file_name = os.path.join(path,file_name)
    print('file name: ', file_name)
    
    file_size = int(connbuf.get_utf8())
    print('file size: ', file_size )
    
    with open(file_name, 'wb') as f:
            remaining = file_size
            while remaining:
                chunk_size = 4096 if remaining >= 4096 else remaining
                chunk = connbuf.get_bytes(chunk_size)
                if not chunk: break
                f.write(chunk)
                remaining -= len(chunk)
            if remaining:
                print('File incomplete.  Missing',remaining,'bytes.')
            else:
                print('File received successfully.')
    return path
def download():
    print('Sending file')
    file_name = connbuf.get_utf8()
    file_name = os.path.join(path,file_name)
    print(file_name)
    if not os.path.isfile(file_name):
        print("File not found")
        connbuf.put_utf8('File not found')
        return path
    connbuf.put_utf8('File found')
    file_size = os.path.getsize(file_name)
    connbuf.put_utf8(str(file_size))
    with open(file_name, 'rb') as f:
            connbuf.put_bytes(f.read())
    return path
    
    
