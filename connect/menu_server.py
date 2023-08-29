import socket
import os
import headers
import buffer


def openMenu(command,con):
    global connbuf
    connbuf = con
    if(command == 'upload'):
        return upload()
    if(command == 'download'):
        return download(text.split(" ")[1])
    if(command == 'mkdir'):
        return makeDIR(text.split(" ")[1])
    if(command == 'cd'):
        return changeDIR(text.split(" ")[1])
    print('Unknown command')
    return ()

def upload():
    file_name = connbuf.get_utf8()
    if '\\' in file_name:
        file_name = file_name.split('\\')[-1]
    print(file_name)
    file_name = os.path.join('d:\\',file_name)
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
    
    
