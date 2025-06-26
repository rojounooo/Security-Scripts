from scapy.all import sniff, IP, TCP # Import necessary Scapy modules for packet sniffing
import requests # To make POST requests to Discord webhook
import os # To load environment variables
from dotenv import load_dotenv # Load environment variables from .env file

load_dotenv() # Load environment variables from .env file
ssh_webhook_url = os.getenv("SSH_URL") # Webhook URL for SSH channel

def send_ssh_alert(ssh_message, ssh_webhook_url):
    data = {
        "content": ssh_message
    }
    try:
        response = requests.post(ssh_webhook_url, json=data)
        if response.status_code != 204:
            print(f"Failed to send alert: {response.status_code} - {response.text}")
    except requests.RequestException as e:
        print(f"Error sending alert: {e}")


def handle_new_connection(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP): # Check if the packet has IP and TCP layers
        # Extract relevant fields from the packet
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        sport = packet[TCP].sport
        dport = packet[TCP].dport

        # Detect only new SSH connection attempts (SYN packets)
        if (dport == 22 or sport == 22) and packet[TCP].flags == 'S':
            alert = f"🚨 SSH Connection Detected!\n🔹 Source: {ip_src}:{sport}\n🔹 Destination: {ip_dst}:{dport}"
            print(alert)
            send_ssh_alert(alert, ssh_webhook_url)

# Start sniffing for TCP traffic
sniff(filter="tcp", prn=handle_new_connection, store=0) # Call handle_new_connection for each packet
# Note: This script requires root privileges to sniff packets on most systems.