import os
import nmap

# Define the subnet to scan
subnet = "192.168.0.0/24"

# Use nmap to scan the subnet for NFS shares
scanner = nmap.PortScanner()
scanner.scan(subnet, arguments="-p 2049")

# Loop through the hosts with open NFS ports
for host in scanner.all_hosts():
  # Check if the host has an open NFS port
  if scanner[host].has_tcp(2049):
    # Print the hostname and IP address of the NFS server
    print(f"Found NFS server: {host} ({scanner[host].hostname()})")

    # Get the list of NFS exports on the server
    exports = scanner[host]["tcp"][2049]["product"].split(",")

    # Loop through the exports
    for export in exports:
      # Mount the NFS export
      print(f"Mounting {export}")
      os.system(f"mount -t nfs {host}:{export} /mnt/{host}_{export.replace('/', '_')}")
