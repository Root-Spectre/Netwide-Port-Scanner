import socket

def run(options):
    target = options.get("target", None)
    port = options.get("p")
    timeout = float(options.get("t", 1))
    fast_mode = options.get("fast", False)
    full_scan = options.get("full", False)

    if not target:
        print("Enter a Target.")

        return

    print(f"Scanning {target}...")
    
    if port:
        port = int(port)
        scan_port(target, port, timeout, True)
    elif fast_mode:
        FAST_PORTS = [
            20,
            21,
            22,
            23,
            25,
            53,
            67,
            68,
            69,
            80,
            88,
            110,
            111,
            113,
            119,
            123,
            135,
            137,
            138,
            139,
            143,
            161,
            162,
            179,
            443,
            445,
            464,
            1433,
            1900,
            2049,
            3000,
            3306,
            3389,
            5000,
            5900,
            8000,
            8080,
            8333,
            8443,
            6379,
            27017,
        ]
        for port in FAST_PORTS:
            scan_port(target, port, timeout, True)
    elif full_scan:
        for port in range(1, 65536):
            scan_port(target, port, timeout, False)
    else:
        for port in range(1, 8888):
            scan_port(target, port, timeout, False)

def scan_port(target, port, timeout, scp):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)

        result = sock.connect_ex((target, int(port)))
        if result == 0:
            print(f"Port {port} Open.")
        else:
            sock.close()
            if scp :
                print(f"Port {port} Closed.")
    except Exception as e:
        print(e)