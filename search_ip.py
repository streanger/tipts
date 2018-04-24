import re

def search_ip(s):
    IP = re.findall(r'[0-9]+(?:\.[0-9]+){3}',s)
    return IP

s = "some 192.168.0.1 example of ip, 127.0.0.1"

print(search_ip(s))
