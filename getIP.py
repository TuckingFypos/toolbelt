#!/usr/bin/env python3

__author__= "TuckingFypos"
__version__= "0.0.2"

import socket
import subprocess
import sys

def main():
    subprocess.call('clear', shell=True)
    localhost = socket.gethostname()
    print("IP will be resolved from " + localhost)
    targetHost = input("Enter a target domain: ")
    targetServer = socket.gethostbyname(targetHost)
    print("The domain " + targetHost + " is hosted at " + targetServer)
    sys.stdout.write(targetServer)

if __name__=="__main__":
    main()

