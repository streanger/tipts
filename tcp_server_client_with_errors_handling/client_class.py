import sys
import time
import socket
from threading import Thread


class TCPClient():
    def __init__(self, target_host, target_port):
        self.target_host = target_host
        self.target_port = target_port
        self.timeout = 5      # [s]
        self.LOCK = False       # lock for retrieving
        self.CONNECTION_STATUS = True
        self.client = self.make_connection(self.target_host, self.target_port)
        if not self.client:
            self.CONNECTION_STATUS = False
        connection_monitor = Thread(target=self.retrieve_connection)
        connection_monitor.start()
        
        
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
        response = '[o] White characters. Not sent.'
        status = False
        
        if not msg.strip():
            return response
            
        if self.LOCK:
            # retrieving connection in progress
            return '[o] No connection with server.'
            
            
        if not self.client:
            # self.client = self.make_connection(self.target_host, self.target_port)
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
            
            
        self.CONNECTION_STATUS = status
        return response
        
        
    def retrieve_connection(self):
        '''check if connection is not lost in loop and then try to retrieve it'''
        while True:
            # print('looking for connection lost')
            if self.CONNECTION_STATUS:
                print("everything's fine")
                time.sleep(0.1)
                continue
                
            self.LOCK = True
            
            while True:
                print('try to retrieve connection')
                self.client = self.make_connection(self.target_host, self.target_port)
                
                if self.client != False:
                    self.CONNECTION_STATUS = True
                    self.LOCK = False
                    break       # go back to monitoring loop
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
        msg = input('put something: ')
        response = client.send_request(msg)
        print(response)
        
    return None
    
    
if __name__ == "__main__":
    client = TCPClient('localhost', 9999)
    client.send_request('hello')
    
    