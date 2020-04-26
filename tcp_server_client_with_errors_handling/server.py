#!/usr/bin/python3
'''server side'''
import sys
import os
import socket


if __name__ == "__main__":
    bind_ip = 'localhost'
    bind_port = 9999
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((bind_ip,bind_port))
    server.listen(5)
    print('[*] Listen on: {}:{}'.format(bind_ip, bind_port))
    
    while True:
        conn, addr = server.accept()
        try:
            print('[*] Connection received from: {}'.format(addr))
            
            while True:
                try:
                    data = conn.recv(16)
                except ConnectionResetError:
                    print('[*] Connection with client broken. Retrying...')
                    break
                    
                if data:
                    decoded = data.decode('utf-8')
                    print('[*] Received data from client: {}'.format(decoded))
                    try:
                        conn.sendall('[*] < Server response >'.encode('utf-8'))
                    except ConnectionResetError:
                        print('[*] Connection broken, by remote host. Retrying...')
                        break
                else:
                    break
        finally:
            conn.close()
