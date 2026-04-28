import socket

def run(options):
    target = options.get("target", None)
    port = options.get("p")

    if not target:
        print("Enter a Target.")

        return
    print(f"Scanning {target}...")
    
    if port:
        port = int(port)
        scan_port(target, port)
    else:
        for port in range(1, 8888):
            scan_range(target, port)
    
def scan_range(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, int(port)))
        if result == 0:
            print(f"Port {port} Open.")

        sock.close()
    except Exception as e:
        print(e)

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, int(port)))
        if result == 0:
            print(f"Port {port} Open.")
        else:
            sock.close()
            print(f"Port {port} Closed.")
    except Exception as e:
        print(e)