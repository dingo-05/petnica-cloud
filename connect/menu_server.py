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
        return makeDIR()
    elif(command == 'cd'):
        return changeDIR()
    elif(command == 'dir'):
        return listDIR()
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
def makeDIR():
    print('Making dir')
    dir_name=connbuf.get_utf8()
    dir_path = os.path.join(path,dir_name)
    if os.path.exists(dir_path):
        connbuf.put_utf8('Directory already exsists')
        return path
    os.makedirs(dir_path)
    connbuf.put_utf8('Directory succesfully created')
    return path
    
def changeDIR():
    print('Changing dir')
    dir_name=connbuf.get_utf8()
    if dir_name=='..' and path==home_path:
        connbuf.put_utf8('Cant go back')
        return path
    elif dir_name=='..':
        array = path.split("\\")
        array.pop()
        dir_path = array[0]
        backslash ='\\'
        for i in range(1,len(array)):
            dir_path = dir_path + backslash + array[i]
        connbuf.put_utf8(dir_path)
        return dir_path
    dir_path = os.path.join(path,dir_name)
    
    if not os.path.exists(dir_path):
        connbuf.put_utf8('Directory not found')
        return path
    connbuf.put_utf8(dir_path)
    return dir_path
def listDIR():
    print('listing directory')
    listing = os.listdir(path)
    print(listing)
    list = ''
    for item in listing:
        list += item + '\n'
    connbuf.put_utf8(list)
    return path