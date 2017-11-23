#!/usr/bin/python3
#fixed somehow :)
import glob
from sys import argv, version, exit

def manual():
    #default_ports should contain all ports available without any external devices
    input("Unplug all virtual port(s) and press enter...")
    defaultPorts = all_ports()
    input("Connect virtual port(s) and press enter...")
    allPorts = all_ports()
    unique = []
    for item in allPorts:
        if not (item in defaultPorts):
            unique.append(item)
    return unique

def all_ports():
    return glob.glob("/dev/tty[A-Za-z]*")

def by_name(name):
    specified = "/dev/tty" + name + "*"
    return  glob.glob(specified)

def help():
	print("Usage:")
	print("  -a, --all -> print all ports")
	print("  -m, --manual -> need to unplug specified device and plug after all")
	print("  -n [string], --name [string] -> with some name e.g. USB")
	print("  -o, --auto -> USB name on default")

def main(argv):
    if (version[0] == "2"):
        print("Please run python3...")
        exit()
    ports = []
    try:
        if argv[0] in ("-a", "--all"):
            ports = all_ports()
        elif argv[0] in ("-m", "--manual"):
            ports = manual()
        elif argv[0] in ("-o, --auto"):
            ports = by_name("USB")
        elif argv[0] in ("-n", "--name"):
            ports = by_name(argv[1])
    except:
        help()
        exit()
    return ports


if __name__=="__main__":
    ports = main(argv[1:])
    print("Ports: ", ports)
