# Subnet Calculator (Beginner Version)

import ipaddress

# Ask user for input
ip_input = input("Enter IP address (example: 192.168.1.10): ")
CIDR=input("Enter CIDR prefix (e.g., 24): ")
try:
    # Create a network object
    network = ipaddress.ip_network(ip_input, strict=False)

    # Get network address
    network_address = network.network_address

    # Get broadcast address
    broadcast_address = network.broadcast_address

    # Total number of IP addresses in this subnet
    total_ips = network.num_addresses

    # Calculate usable hosts
    if network.prefixlen >= 31:
        usable_hosts = 0
    else:
        usable_hosts = total_ips - 2

    # Print results
    print("\nSubnet Results:")
    print("Network Address:", network_address)
    print("Broadcast Address:", broadcast_address)
    print("Usable Hosts:", usable_hosts)

except:
    print("Invalid input! Please try again.")