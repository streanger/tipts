#run with using pyhton3
#still in develop :)
#need to clean this up and make usefull :)
import glob
import getopt
from sys import argv, version, exit

def unique_man(defaultPorts=[]):
    #default_ports should contain all ports available without any external devices
    if not defaultPorts:
        defaultPorts = find_default_ports()
        #defaultPorts = ['/dev/ttyprintk', '/dev/ttyS31', '/dev/ttyS30', '/dev/ttyS29', '/dev/ttyS28', '/dev/ttyS27', '/dev/ttyS26', '/dev/ttyS25', '/dev/ttyS24', '/dev/ttyS23', '/dev/ttyS22', '/dev/ttyS21', '/dev/ttyS20', '/dev/ttyS19', '/dev/ttyS18', '/dev/ttyS17', '/dev/ttyS16', '/dev/ttyS15', '/dev/ttyS14', '/dev/ttyS13', '/dev/ttyS12', '/dev/ttyS11', '/dev/ttyS10', '/dev/ttyS9', '/dev/ttyS8', '/dev/ttyS7', '/dev/ttyS6', '/dev/ttyS5', '/dev/ttyS4', '/dev/ttyS3', '/dev/ttyS2', '/dev/ttyS1', '/dev/ttyS0']
    ports = all_ports()
    unique = []
    for item in ports:
        if not (item in defaultPorts):
            unique.append(item)
    return unique

def all_ports():
    return glob.glob("/dev/tty[A-Za-z]*")

def auto_find():
    return glob.glob("/dev/ttyUSB*")

def named_ports(name):
    specified = "/dev/tty" + name + "*"
    return  glob.glob(specified)

def find_default_ports():
    input("Unplug all virtual port(s) and press enter...")
    defaultPorts = glob.glob("/dev/tty[A-Za-z]*")
    input("Connect virtual port(s)")
    return defaultPorts

def main(argv):
    ports = []
    if version[0] == "2":
        print("--< please run with python3")
        exit()
    try:
        opts, args = getopt.getopt(argv, "h:u:a:",
        ["help", "unique", "all"])
    except getopt.GetoptError as err:
        print(str(err))
        opts = ('-h')
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("usage:")
            print("--all -> print all ports")
            print("--unique -> need to unplug specified device and plug after all")
            print("--name -> with some name e.g. USB")
            print("--auto -> USB name on default")
            exit()
        elif opt in '-u':
            ports = named_ports(arg)
        elif opt in '-a':
            ports = all_ports()

    #find ports in different way and print after all
    print("--<",ports)

if __name__=="__main__":
    main(argv[1:])
