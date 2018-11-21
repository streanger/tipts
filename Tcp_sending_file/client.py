import sys
import os
import socket               # Import socket module

def script_path():
    '''change current path to script one'''
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(path)
    return path

def send_file(file):
    path = script_path()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
    # host = socket.gethostname()     # Get local machine name
    host = "localhost" # Get local machine name
    # host = "" # Get local machine name
    port = 0                 # Reserve a port for your service.
    port = 8080                 # Reserve a port for your service.

    s.connect((host, port))
    # s.send("Hello server!".encode("utf-8"))
    f = open(file,'rb')
    print('Sending...')
    l = f.read(1024)
    while (l):
        # print('Sending...')
        s.send(l)
        l = f.read(1024)
    f.close()
    print("Done Sending")
    s.shutdown(socket.SHUT_WR)
    print(s.recv(1024))
    s.close                     # Close the socket when done
    return True
    
    
if __name__ == "__main__":
    file = 'pigeon.png'
    send_file(file)
    
    
    
    
    
    