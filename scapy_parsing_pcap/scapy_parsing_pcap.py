from scapy.utils import RawPcapReader
from scapy.all import *


if __name__ == "__main__":
    filename = 'file.pcap'
    scapy_cap = rdpcap(filename)
    for packet in scapy_cap:
        src_ip = packet[IP].src
        if not packet[DNS].qr:
            dns_query = packet[DNSQR].qname
            print(dns_query.decode('utf-8'))
            