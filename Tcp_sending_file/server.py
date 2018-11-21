import sys
import os
import socket               # Import socket module

def script_path():
    '''change current path to script one'''
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(path)
    return path

def receive_file(file):    
    path = script_path()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
    # host = socket.gethostname() # Get local machine name
    host = "localhost" # Get local machine name
    # host = "" # Get local machine name
    port = 8080                 # Reserve a port for your service.
    s.bind((host, port))        # Bind to the port
    selected = s.getsockname()
    f = open(file,'wb')
    s.listen(5)                 # Now wait for client connection.
    while True:
        c, addr = s.accept()     # Establish connection with client.
        print('Got connection from', addr)
        print("Receiving...")
        l = c.recv(1024)
        while (l):
            # print("Receiving...")
            f.write(l)
            l = c.recv(1024)
        f.close()
        print("Done Receiving")
        # c.send('Thank you for connecting'.encode("utf-8"))
        c.shutdown(socket.SHUT_WR)
        c.close()                # Close the connection
        break
    s.close()    
    return True
    
    
if __name__ == "__main__":
    file = 'pigeon2.png'
    status = receive_file(file)
    print(status)
    
    