# Workspace README

## Overview

This workspace contains several Python scripts and small projects related to network utilities, log analysis, validation checks, and simple web clients.

## Files and Purpose

- `ip_validator.py` - IPv4 subnet calculator that accepts an IP address and CIDR prefix, then prints the network address, broadcast address, and usable hosts count.
- `name_pridictor.py` - Basic IPv4 format validator that checks whether user input matches a valid dotted-quad address.
- `task2.py` - Firewall log parser and analyzer. Reads `firewall.log`, writes `output.csv` and `output.json`, and saves a threat report to `threats.txt`.
- `task3.py` - Another firewall log parser and analyzer with the same behavior as `task2.py`, producing CSV, JSON, and threat report output.
- `task5.py` - SSH connection example using `paramiko`. Connects to a device using an SSH key and runs a simple command.
- `task6.py` - Network device backup script using `netmiko`. Connects to listed Cisco devices and saves running configuration backups into the `backups/` directory.
- `project.py` - Combined network audit tool. Uses Netmiko and Paramiko to retrieve device configs, audits them for telnet/http/snmp settings, and saves an audit report under `reports/`.
- `webclient.py` - Simple HTTP client example that sends a GET request to a configured local endpoint and prints JSON output.
- `test.py` - Flask web application for predicting nationality from a name using the `nationalize.io` API and rendering output with `templates/index.html` and `templates/results.html`.
- `error_test.py` - Input validation example demonstrating exception handling for integer conversion.
- `t3.py` - Python list mutation example showing how list aliasing and concatenation behave.
- `tt.py` - Empty placeholder file.

## Supporting Files and Directories

- `firewall.log` - Input file used by `task2.py` and `task3.py`.
- `output.csv` - Output from firewall log analysis scripts.
- `output.json` - Output from firewall log analysis scripts.
- `threats.txt` - Threat report output from firewall log analysis scripts.
- `backups/` - Directory where `task6.py` stores device configuration backups.
- `reports/` - Directory where `project.py` saves audit reports.
- `templates/` - HTML templates used by `test.py`.

## Requirements

Recommended Python packages:

- `Flask`
- `requests`
- `pycountry`
- `paramiko`
- `netmiko`

Install dependencies with:

```bash
python -m pip install Flask requests pycountry paramiko netmiko
```

## Usage

Run each script directly with Python. Examples:

```bash
python ip_validator.py
python name_pridictor.py
python task2.py
python task3.py
python task5.py
python task6.py
python project.py
python webclient.py
python test.py
python error_test.py
python t3.py
```

### Notes

- `task5.py`, `task6.py`, and `project.py` require real device IPs and credentials to work. Update the placeholder values before running.
- `test.py` runs a Flask web server and requires the `templates/` directory to be present.
- `task2.py` and `task3.py` both operate on `firewall.log` and generate the same set of outputs.

## Suggested Next Steps

- Add a `requirements.txt` file to simplify package installation.
- Standardize duplicate scripts (`task2.py` and `task3.py`) if they are intended to serve the same task.
- Add comments or docstrings in scripts to explain expected inputs and outputs more clearly.
