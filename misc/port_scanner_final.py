import socket
    
# Scan ports    
def scan_port(host, port):
    # Create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Set a timeout of 1 second so the scan doesn't hang
    sock.settimeout(1)
    try:
        # Attempt to connect to host
        result = sock.connect_ex((host, port))
        # If result is 0 the port is open
        if result == 0:
            print(f"Port {port} is OPEN")
        else:
            print(f"Port {port} is CLOSED")
    except socket.gaierror:
        # Handle if host is unreachable
        print(f"Host {host} is unreachable")
        return
    finally:
        # Close connection when done
        sock.close()
# Scan range of IPs and the given host
def scan_ports(host, start, end):
    print(f"Scanning {host} on ports {start} to {end}")
    #Loop through and scan each port in range
    for port in range(start, end + 1):
        scan_port(host,port)

def main():
    # Target host
    host = "scanme.nmap.org"
    try:
        # As user for start and end ports
        start = int(input("Start port: "))
        end = int(input("End port: "))
    except ValueError:
        # Handle error if ports arnt numbers
        print("Ports nust be numbers.")
        return
    # Call the function to start scanning port range
    scan_ports(host, start, end)

# Check if script is being run directly
if __name__ == '__main__':
    main()
