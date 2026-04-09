import paramiko
from datetime import datetime


devices = [
    {"name": "routerA", "ip": "192.168.100.11", "username": "admin", "password": "password"},
    {"name": "routerB", "ip": "192.168.100.16", "username": "admin", "password": "password"},
]

def get_running_config(device):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(device["ip"], username=device["username"], password=device["password"], timeout=5)

        stdin, stdout, stderr = ssh.exec_command("show running-config")
        config = stdout.read().decode()

        ssh.close()
        return config
    except Exception as e:
        return None

def audit_device(config):
    results = {}

    # Telnet check
    if "line vty" in config and "transport input telnet" in config:
        results["telnet"] = "Telnet is enabled"
    else:
        results["telnet"] = "Telnet is disabled"

    # HTTP server check
    if "ip http server" in config:
        results["http"] = "HTTP server is enabled"
    else:
        results["http"] = "HTTP server is disabled"

    # SNMP check
    if "snmp-server community public" in config or "snmp-server community private" in config:
        results["snmp"] = "Default SNMP community strings found"
    else:
        results["snmp"] = "No default SNMP community strings found"

    return results

def generate_report(audit_results):
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"Audit_Report_{date_str}.txt"

    with open(filename, "w") as file:
        file.write("--- Network Device Audit Report ---\n")

        for device_name, results in audit_results.items():
            file.write(f"\nDevice: {device_name}\n")
            file.write(f"- Telnet Status: {results['telnet']}\n")
            file.write(f"- HTTP Server Status: {results['http']}\n")
            file.write(f"- SNMP Status: {results['snmp']}\n")

    print(f"Audit report saved to {filename}")

def main():
    audit_results = {}

    for device in devices:
        config = get_running_config(device)

        if config:
            results = audit_device(config)
        else:
            results = {
                "telnet": "Unable to retrieve config",
                "http": "Unable to retrieve config",
                "snmp": "Unable to retrieve config"
            }

        audit_results[device["name"]] = results

    generate_report(audit_results)

if __name__ == "__main__":
    main()