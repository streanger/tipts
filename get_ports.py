#run with using pyhton3
#still in develop :)
import glob
from sys import argv, version, exit

def list_ports(uniqueOnly=False, randomPorts=[]):
    #default_ports should contain all ports available without any external
    defaultPorts = []
    if not randomPorts:
        defaultPorts = find_default_ports()
        #defaultPorts = ['/dev/ttyprintk', '/dev/ttyS31', '/dev/ttyS30', '/dev/ttyS29', '/dev/ttyS28', '/dev/ttyS27', '/dev/ttyS26', '/dev/ttyS25', '/dev/ttyS24', '/dev/ttyS23', '/dev/ttyS22', '/dev/ttyS21', '/dev/ttyS20', '/dev/ttyS19', '/dev/ttyS18', '/dev/ttyS17', '/dev/ttyS16', '/dev/ttyS15', '/dev/ttyS14', '/dev/ttyS13', '/dev/ttyS12', '/dev/ttyS11', '/dev/ttyS10', '/dev/ttyS9', '/dev/ttyS8', '/dev/ttyS7', '/dev/ttyS6', '/dev/ttyS5', '/dev/ttyS4', '/dev/ttyS3', '/dev/ttyS2', '/dev/ttyS1', '/dev/ttyS0']
    else:
        defaultPorts = randomPorts
    ports = glob.glob("/dev/tty[A-Za-z]*")
    unique = []
    for item in ports:
        if not (item in defaultPorts):
            unique.append(item)
    if uniqueOnly:
        return unique
    return ports

def auto_find():
    return glob.glob("/dev/ttyUSB*")

def find_default_ports():
    input("Unplug all virtual port(s) and press enter...")
    defaultPorts = glob.glob("/dev/tty[A-Za-z]*")
    input("Connect virtual port(s)")
    return defaultPorts

def get_ports(args):
    if version[0] == "2":
        print("--< please run with python3")
        exit()

    #find ports in different way and print after all
    if args:
        ports = list_ports()
    else:
        ports = auto_find()
    print("--<",ports)

if __name__=="__main__":
    get_ports(argv[1:])
