import sys
import socket
import threading

# Check if the IP address is provided as a command-line argument
if len(sys.argv) < 2:
    print("Usage: python3 file.py <ip>")
    sys.exit(1)

# Get the IP address from the command-line argument
ip = sys.argv[1]

# Scan all possible ports
ports = range(1, 65536)

# Define a function to scan a single port


def scan_port(port):
    try:
        # Connect to the port
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            s.connect((ip, port))
            print(f"Port {port} is open")
    except:
        pass


# Create multiple threads to scan ports concurrently
threads = []
for port in ports:
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()
