# This script is a simple port scanner that checks for open ports on a given target using Python's nmap library.
# This script requires the nmap tool to be installed on the system.

# Import necessary libraries
import nmap
import sys 

# Check for arguments 

if len(sys.argv) != 2:
    print("Usage: python3 port_scanner.py <host>")
    sys.exit(1)

else:
    target = sys.argv[1]

# Create a PortScanner object and scan the target for open ports

scanner = nmap.PortScanner()
scanner.scan(hosts=target, arguments='-p 1-65535')

for host in scanner.all_hosts():
    print(f"Scanning host: {host}")
    for proto in scanner[host].all_protocols():
        print(f"Protocol: {proto}")
        lport = scanner[host][proto].keys()
        for port in sorted(lport):
            state = scanner[host][proto][port]['state']
            print(f"Port: {port}\tState: {state}")