# Python script that resolves hostnames from a list of ip-addresses from text-file and exports the result to a csv-file.

import socket
import csv

# Resolve hostname from IP
def resolve_hostname(ip_address):
    try:
        hostname = socket.gethostbyaddr(ip_address)[0]
    except socket.herror:
        hostname = "Unknown"
    return hostname

# Read IP-addresses from file and loop through each IP address
with open('ip_addresses.txt', 'r') as file:
    ip_addresses = file.read().splitlines()

    resolved_data = []
    for ip in ip_addresses:
        hostname = resolve_hostname(ip)
        resolved_data.append((ip, hostname))

# Write the data to CSV
with open('resolved_hostnames.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['IP Address', 'Hostname'])
    csvwriter.writerows(resolved_data)

print("Resolved hostnames have been written to resolved_hostnames.csv")
