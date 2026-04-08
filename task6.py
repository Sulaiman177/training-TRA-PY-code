from netmiko import ConnectHandler, NetMikoTimeoutException, NetMikoAuthenticationException
from datetime import datetime
import os

# Example list of devices
devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.1",
        "username": "admin",
        "password": "password123"
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.2",
        "username": "admin",
        "password": "password123"
    }
]

# Directory to store backups
backup_dir = "backups"
os.makedirs(backup_dir, exist_ok=True)

# Get current date for file naming
current_date = datetime.now().strftime("%Y-%m-%d")

for device in devices:
    try:
        print(f"Connecting to {device['ip']}...")
        # Establish SSH connection
        connection = ConnectHandler(**device)
        
        # Get hostname from device prompt
        hostname = connection.find_prompt().strip('#').strip()
        print(f"Backing up configuration for {hostname}...")

        # Retrieve running configuration
        running_config = connection.send_command("show running-config")
        
        # Build backup filename
        filename = f"{hostname}_{current_date}.txt"
        filepath = os.path.join(backup_dir, filename)
        
        # Save configuration to file
        with open(filepath, "w") as file:
            file.write(running_config)
        
        print(f"Backup successful: {filepath}")
        connection.disconnect()
    except (NetMikoTimeoutException, NetMikoAuthenticationException) as e:
        print(f"Failed to connect to {device['ip']}: {e}")
    except Exception as e:
        print(f"Error with {device['ip']}: {e}")

print("All device backups completed.")