#!/usr/bin/python3
#server side
import socket
import re
import sys
import threading

def handle_client(client_socket):
    request = client_socket.recv(1024).decode('utf-8')
    print("<> Odebrano: {}".format(request))
    client_socket.send("ACK!".encode('utf-8'))
    client_socket.close()
    return True
    
    
if __name__ == "__main__":
    bind_ip = "0.0.0.0"
    bind_port = 9999
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((bind_ip,bind_port))
    server.listen(5)
    print("Nasluchiwanie na porcie {}:{}".format(bind_ip, bind_port))
    
    while True:
        client, addr = server.accept()
        print("<> Przyjeto polaczenie od: {}:{}".format(addr[0], addr[1]))
        
        #utworzenie watku obslugi clienta
        client_handler = threading.Thread(target=handle_client, args=(client, ))
        client_handler.start()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    