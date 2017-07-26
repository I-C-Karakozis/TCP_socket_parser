import socket

# specify IP address, port and buffer size
TCP_IP = '127.0.0.1'
TCP_PORT = 8080
BUFFER_SIZE = 1024

def read_tcp():
    """
    Function listening to tcp connectiong and "reading" the incoming content line by line
    """
    # many tcp connections require you to send a hello message to connect
    s.send('hello_message')   

    # keep reading content of size BUFFER_SIZE until you exhaust the content sent
    buffer = s.recv(BUFFER_SIZE)
    buffering = True
    
    while buffering:
        if "\n" in buffer:
            # read and print a line at a time
            (line, buffer) = buffer.split("\n", 1)
            print line
        else:
            # append incoming content once buffer is exhausted
            more = s.recv(BUFFER_SIZE)
            if not more:
                buffering = False
            else:
                buffer = buffer + more


if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    read_tcp()
    s.close()
