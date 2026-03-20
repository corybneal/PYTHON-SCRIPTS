# Network Scanner
# Cory Neal - Cybersecurity & AI


import socket

def scan_port(host,port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host,port))
        sock.close()
        if result == 0:
            print(f"Port {port} - OPEN")
        else:
            print(f"Port {port} - CLOSED")
    except Exception as e:
        print(f"Error: {e}")

# Scan your local machine
host = "127.0.0.1"
ports = [21, 22, 23, 80, 443, 3306, 8080]

print(f"\nScanning {host}...")
print("=" * 30)
for port in ports:
    scan_port(host,port)
print("=" * 30)
print("Scan Complete!")