import socket

def scan_ports(host, ports):
    print(f"\n🔎 Scanning {host} on ports: {ports}\n")
    for port in map(int, ports.split(',')):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((host, port))
            if result == 0:
                print(f"✅ Port {port} is OPEN")
            else:
                print(f"❌ Port {port} is CLOSED or FILTERED")
