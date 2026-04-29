import socket
from concurrent.futures import ThreadPoolExecutor

def run(options):
    try:
        target = options.get("target", None)
        port = options.get("p")
        timeout = float(options.get("t", 1))
        threads = int(options.get("threads", 200))
        fast_mode = options.get("fast", False)
        full_scan = options.get("full", False)

        if not target:
            print("Enter a Target.")

            return

        print(f"Scanning {target}...")
        
        if port:
            port = int(port)
            scan_port(target, port, timeout, True)
            print("Scan Finished.")
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

            with ThreadPoolExecutor(max_workers=threads) as executor:
                for port in FAST_PORTS:
                    executor.submit(scan_port, target, port, timeout, True)

            print("Scan Finished.")
        elif full_scan:
            with ThreadPoolExecutor(max_workers=threads) as executor:
                for port in range(1, 65536):
                    executor.submit(scan_port, target, port, timeout, False)

            print("Scan Finished.")
        else:
            with ThreadPoolExecutor(max_workers=threads) as executor:
                for port in range(1, 10000):
                    executor.submit(scan_port, target, port, timeout, False)

            print("Scan Finished.")
    except KeyboardInterrupt:
        print("Scan Interrupted.")

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