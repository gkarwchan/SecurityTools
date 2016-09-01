#!/usr/bin/env python3.5
import socket
import subprocess
import sys
from datetime import datetime

remoteServer = input("Enter a remote host to scan (example google.com): ")
remoteServerIP = socket.gethostbyname(remoteServer)

print ("IP4 address for the server is:" , remoteServerIP)
socket.setdefaulttimeout(0.1)
try:
    for port in range(1, 1025):
        print("testing port {}: \t".format(port), end="", flush=True)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("is open")
        else:
            print("is close")
        sock.close()

except socket.gaierror:
    print ("Hostname could not be resolved")
    sys.exit()

except socket.error:
    print("Cannot connect to the server")
    sys.exit()