import paramiko

# Replace with your device details
hostname = "your_device_ip"
username = "your_username"
key_path = "/home/your_local_user/.ssh/id_rsa_paramiko"

def ssh_connect():
    try:
        # Create SSH client
        client = paramiko.SSHClient()
        
        # Automatically add unknown host keys
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Load private key
        private_key = paramiko.RSAKey.from_private_key_file(key_path)

        # Connect using SSH key
        client.connect(
            hostname=hostname,
            username=username,
            pkey=private_key,
            timeout=10
        )

        print(f"✅ Successfully connected to {hostname} using SSH key.")

        # Run a simple command
        stdin, stdout, stderr = client.exec_command("uname -a")

        print("\n📤 Command Output:")
        print(stdout.read().decode())

        print("⚠️ Errors (if any):")
        print(stderr.read().decode())

        # Close connection
        client.close()

    except Exception as e:
        print(f"❌ Connection failed: {e}")

if __name__ == "__main__":
    ssh_connect()