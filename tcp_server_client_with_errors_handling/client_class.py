import sys
import time
import socket



class TCPClient():
    def __init__(self, target_host, target_port):
        self.target_host = target_host
        self.target_port = target_port
        self.timeout = 10      # [s]
        self.client = self.make_connection(self.target_host, self.target_port)
        
        
    def make_connection(self, target_host, target_port):
        begin = time.time()
        while True:
            if (time.time() - begin) > self.timeout:
                return False
            try:
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.connect((target_host, target_port))
                break
            except:
                print('[o] Fail to connect', end='\r', flush=True)
                continue
        return client
        
        
    def send_request(self, msg):
        if not msg.strip():
            return '[o] (empty)'
            
        response = '[o] (empty)'
        status = False
        
        if not self.client:
            self.client = self.make_connection(self.target_host, self.target_port)
            return '[o] Failed to connect to server'
            
            
        try:
            self.client.send(msg.encode('utf-8'))
        except ConnectionResetError:
            response = '[o] Connection broken. Retrying...'
            
        except ConnectionAbortedError:
            response = '[o] Connection broken. Retrying...'
            
            
        try:
            response = self.client.recv(4096).decode('utf-8')
            status = True
        except ConnectionResetError:
            response = '[o] Connection reset error'
            
            
        if not status:
            # try to retrieve connection
            self.client = self.make_connection(self.target_host, self.target_port)
            
        return response
        
        
def example():
    '''
    just create client and send msg to server
    '''
    client = TCPClient('localhost', 9999)
    response = client.send_request('message')
    print(response)
    return None
    
    
def loop_example():
    global DEBUG
    DEBUG = True
    if DEBUG:
        target_host, target_port = 'localhost', 9999
    else:
        target_host, target_port = '1.2.3.4', 23
        
        
    client = TCPClient(target_host, target_port)
    while True:
        msg = input('send something: ')
        response = client.send_request(msg)
        print(response)
    return
    
    
if __name__ == "__main__":
    # loop_example()
    example()
    
    