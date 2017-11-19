import glob

def list_ports(uniqueOnly=False, randomPorts=[]):
    #default_ports should contain all ports available without any external
    defaultPorts = []
    if not randomPorts:
        defaultPorts = ['/dev/ttyprintk', '/dev/ttyS31', '/dev/ttyS30', '/dev/ttyS29', '/dev/ttyS28', '/dev/ttyS27', '/dev/ttyS26', '/dev/ttyS25', '/dev/ttyS24', '/dev/ttyS23', '/dev/ttyS22', '/dev/ttyS21', '/dev/ttyS20', '/dev/ttyS19', '/dev/ttyS18', '/dev/ttyS17', '/dev/ttyS16', '/dev/ttyS15', '/dev/ttyS14', '/dev/ttyS13', '/dev/ttyS12', '/dev/ttyS11', '/dev/ttyS10', '/dev/ttyS9', '/dev/ttyS8', '/dev/ttyS7', '/dev/ttyS6', '/dev/ttyS5', '/dev/ttyS4', '/dev/ttyS3', '/dev/ttyS2', '/dev/ttyS1', '/dev/ttyS0']
        #print("--< default as well")
    else:
        defaultPorts = randomPorts
        #print("--< specified ports as default")
    ports = glob.glob("/dev/tty[A-Za-z]*")
    unique = []
    for item in ports:
        if not (item in defaultPorts):
            unique.append(item)
    if uniqueOnly:
        return unique
    return ports

#print(list_ports(uniqueOnly=True, randomPorts=['/dev/ttyprintk']))
print(list_ports(uniqueOnly=True))
