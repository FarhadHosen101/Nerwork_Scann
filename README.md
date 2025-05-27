# Network IP & MAC Address Scanner

A simple Python tool to scan local networks and find all connected devices' IP and MAC addresses using ARP requests.

## 🔧 How It Works
- Sends ARP requests across a target IP range.
- Collects IP and MAC addresses from all active devices on the network.

## 📦 Requirements
- Python 3
- `scapy` library

## Usage
Using:
-```bash
python scanner.py -t <target ip>`

Install scapy:
```bash
pip install scapy
