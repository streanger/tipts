#!/usr/bin/python3
'''client side'''
import sys
import os
import socket


if __name__ == "__main__":
    # target_host, target_port = '169.254.227.138', 23
    target_host, target_port = 'localhost', 9999
    
    while True:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((target_host, target_port))
        except:
            print('[o] Fail to connect', end='\r', flush=True)
            continue
            
        while True:
            msg = input("[o] Send message: ")
            if not msg.strip():
                continue
                
            if msg in ('quit', 'close', 'exit', 'end', 'finish'):
                print('closing connection')
                client.close()
                sys.exit()
                
            try:
                client.send(msg.encode('utf-8'))
            except ConnectionResetError:
                print('[o] Connection broken. Retrying...')
                break
                
            response = client.recv(4096).decode('utf-8')
            print(response)
