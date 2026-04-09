import ipaddress

# Ask user for input
ip_input = input("Enter IP address (example: 192.168.1.10): ")
cidr_input = input("Enter CIDR prefix (e.g., 24): ")

try:
    # Combine IP and CIDR
    network = ipaddress.ip_network(f"{ip_input}/{cidr_input}", strict=False)

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
    print("\n--- Subnet Calculator ---")
    print("Network Address:", network_address)
    print("Broadcast Address:", broadcast_address)
    print("Number of Usable Hosts:", usable_hosts)
    print("-------------------------")

except ValueError as e:
    print("\n--- Subnet Calculator ---")
    print(f"Error: Invalid IP address or CIDR prefix provided. Details: {e}")
    print("-------------------------")



# Subnet Calculator (Beginner Version)

"""import ipaddress

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
    print("Invalid input! Please try again.")"""




"""import ipaddress

def subnet_calculator():
    print("--- Subnet Calculator ---")
    
    try:
        ip_input = input("Enter an IP address (e.g., 192.168.1.1): ").strip() # Ask user for input
        cidr_input = input("Enter CIDR prefix (e.g., 24): ").strip()
        
        # Convert CIDR to integer (this will catch non-numeric input)
        cidr = int(cidr_input)
        
        # Create network object (strict=False allows host IPs)
        network = ipaddress.IPv4Network(f"{ip_input}/{cidr}", strict=False)
        
        network_address = network.network_address
        broadcast_address = network.broadcast_address
        
        # Calculate usable hosts
        if network.num_addresses <= 2:
            usable_hosts = 0
        else:
            usable_hosts = network.num_addresses - 2
        
        print(f"Network Address: {network_address}")
        print(f"Broadcast Address: {broadcast_address}")
        print(f"Number of Usable Hosts: {usable_hosts}")
    
    except ValueError as e:
        print(f"Error: Invalid IP address or CIDR prefix provided. Details: {e}")
    
    print("-------------------------")

if __name__ == "__main__":
    subnet_calculator()"""