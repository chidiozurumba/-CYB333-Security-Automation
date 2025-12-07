import socket

def main():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server on localhost and port 9999
        client.connect(("localhost", 9999))

        # Send a message to the server
        client.sendall("Hello from client".encode())

        # Receive a reply from the server
        data = client.recv(1024)
        if data:
            print(f"Server says: {data.decode()}")

    except socket.error as error:
        print(f"Socket error: {error}")

    finally:
        # Always close the socket
        client.close()
        print("Client socket closed cleanly.")

if __name__ == "__main__":
    main()
