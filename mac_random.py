import random
import time

def random_mac():
    mac = [hex(random.randrange(255))[2:] for x in range(6)]
    mac = ["0"*(len(item)%2)+item for item in mac]
    return ":".join(mac)

print(random_mac())
