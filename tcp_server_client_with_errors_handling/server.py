#!/usr/bin/python3
'''server side'''
import sys
import os
import socket


if __name__ == "__main__":
    # bind_ip, bind_port = '169.254.227.138', 23
    bind_ip, bind_port = 'localhost', 9999
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((bind_ip,bind_port))
    except:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.listen(5)
    print('[*] Listen on: {}:{}'.format(bind_ip, bind_port))
    
    while True:
        conn, addr = server.accept()
        try:
            print('[*] Connection received from: {}'.format(addr))
            
            while True:
                try:
                    data = conn.recv(4096)
                    
                except ConnectionResetError:
                    print('[*] Connection with client broken. Retrying...')
                    break
                    
                if data:
                    try:
                        decoded = data.decode('utf-8')
                        
                    except UnicodeDecodeError as err:
                        print('[*] Error catched: {}'.format(err))
                        continue
                        
                    print('[*] Received data from client: {}'.format(decoded))
                    try:
                        conn.sendall('[*] < Server response >'.encode('utf-8'))
                        
                    except ConnectionResetError:
                        print('[*] Connection broken, by remote host. Retrying...')
                        break
                else:
                    print('no data')
                    break
        finally:
            conn.close()
