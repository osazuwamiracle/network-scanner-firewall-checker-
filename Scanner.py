import socket

def scan_port(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((host, port))
        s.close()
        return result == 0
    except:
        return False

host = input("Enter host to scan (e.g. 127.0.0.1): ")
common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3389, 8080]
print(f"\nScanning {host}...\n")

for port in common_ports:
    status = "OPEN - CHECK FIREWALL!" if scan_port(host, port) else "Closed"
    print(f"Port {port}: {status}")
  
