# nfs-scanner

⠀⠀⠀⠀⠐⣶⣶⣦⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣤⣀⡀⠀⠀⠀⠀⠀
⠀⣠⣤⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⠀⠀⠀
⠈⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀
⠀⠀⠀⠀⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠻⠿⠋⠘⣿⣿⣿⡄⠀
⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⢹⡏⠀⠀⠀⠀⠀⢿⣿⣿⡇⠀
⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⠨⢇⡀⠀⠀⠀⡠⠜⢸⣿⣷⠀
⠀⠀⠉⢰⣿⣿⡿⣿⣿⣿⣿⡟⠻⣿⠖⠀⠀⠀⠺⣿⢾⣿⣿⠀NFS - SCAN & MOUNT
⠀⠀⠀⣾⣿⣿⡇⢻⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠻⠆
⠀⠀⠀⠋⠉⣿⣷⣼⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀
⠀⠀⠀⠀⠀⢻⣿⢿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⣀⣠⣿⣿⠀⠀
⠀⠀⠀⠀⠀⠈⠁⠀⣿⡿⣿⡿⠓⠒⠒⠒⠒⠋⠁⠙⢿⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠏⠀⠙⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠀⠀

This script uses the nmap library to scan the specified subnet for hosts with open NFS ports (port 2049). It then loops through the hosts with open NFS ports and prints their hostnames and IP addresses.

The script also gets the list of NFS exports on each server by parsing the product field of the NFS service. It then uses the os module to mount each NFS export using the mount command. The mountpoint is created using the hostname and the export name, with the slashes in the export name replaced with underscores to avoid any issues with the filesystem path.

To use this script, you would need to replace 192.168.0.0/24 with the actual subnet you want to scan, and adjust the mountpoint path as needed (e.g. /mnt/nfs). You can then run the script and it will scan the subnet for NFS servers, print their information, and mount their exports. Note that this script assumes that you have the necessary permissions to scan the network and mount NFS shares on the system.
