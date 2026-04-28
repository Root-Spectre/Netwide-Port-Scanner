import socket

def run(options):
    target = options.get("target", None)
    port = options.get("p")
    timeout = float(options.get("t", 1))

    if not target:
        print("Enter a Target.")

        return

    print(f"Scanning {target}...")
    
    if port:
        port = int(port)
        scan_port(target, port, timeout)
    else:
        for port in range(1, 8888):
            scan_range(target, port, timeout)
    
def scan_range(target, port, timeout):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)

        result = sock.connect_ex((target, int(port)))
        if result == 0:
            print(f"Port {port} Open.")

        sock.close()
    except Exception as e:
        print(e)

def scan_port(target, port, timeout):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)

        result = sock.connect_ex((target, int(port)))
        if result == 0:
            print(f"Port {port} Open.")
        else:
            sock.close()
            print(f"Port {port} Closed.")
    except Exception as e:
        print(e)