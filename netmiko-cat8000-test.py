"""
netmiko-cat8000-test.py

Quick connectivity test against the Cisco DevNet
"Catalyst 8000 Always-On Sandbox" using Netmiko.

Setup:
    pip install netmiko --break-system-packages

Usage:
    1. Fill in HOST, USERNAME, PASSWORD below with the credentials
       generated when you launched the sandbox.
    2. Run from your Codespaces terminal:
           python netmiko-cat8000-test.py
"""

from netmiko import ConnectHandler
from netmiko import NetmikoTimeoutError, NetmikoAuthenticationException

HOST = "REPLACE_WITH_SANDBOX_IP"
PORT = 22
USERNAME = "REPLACE_WITH_USERNAME"
PASSWORD = "REPLACE_WITH_PASSWORD"

device = {
    "device_type": "cisco_xe",
    "host": HOST,
    "port": PORT,
    "username": USERNAME,
    "password": PASSWORD,
    "fast_cli": False,  # safer default for sandbox/lab devices
}


def main():
    print(f"connecting to {HOST}:{PORT} ...")
    try:
        conn = ConnectHandler(**device)
    except NetmikoAuthenticationException:
        print("auth failed - check username/password")
        return
    except NetmikoTimeoutError:
        print("connection timed out - check host/port and that the sandbox is active")
        return

    print("connected. running 'show version'...\n")
    output = conn.send_command("show version")
    print(output)

    print("\nrunning 'show ip interface brief'...\n")
    output = conn.send_command("show ip interface brief")
    print(output)

    conn.disconnect()
    print("\ndisconnected.")


if __name__ == "__main__":
    main()
