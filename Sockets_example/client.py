#!/usr/bin/python3
#client side
import socket
import re
import sys


if __name__ == "__main__":
    target_host = "localhost"
    target_port = 9999
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_host, target_port))
    
    msg = input("send message: ")
    client.send(msg.encode('utf-8'))
    response = client.recv(4096).decode('utf-8')
    print(response)