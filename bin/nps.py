import socket

def run(options):
    target = options.get("target", None)
    print(f"Scanning {target}...")

    for port in range(1, 1000):
        scan_port(target, port)
    
def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_SEQPACKET)
        sock.settimeout(15)

        result = sock.connect_ex((target, int(port)))
        if result == 0:
            print(f"Port {port} Open.")

        sock.close()
    except Exception as e:
        print(e)