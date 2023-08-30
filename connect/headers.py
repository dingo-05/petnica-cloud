HEADER_LEN = 4
NAME_LEN = 32

def appendHeaders(message):
    message = message.encode('utf-8')
    return len(message).to_bytes(HEADER_LEN) + message
        
        