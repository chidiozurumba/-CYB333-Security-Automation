import socket

def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Bind server to localhost on port 9999
        server.bind(("localhost", 9999))

        # Start listening for incoming connections
        server.listen(1)
        print("Server is listening...")

        # Accept a client connection
        conn, addr = server.accept()
        print(f"Connected to {addr}")

        # Receive data from client
        data = conn.recv(1024)
        if data:
            print(f"Client says: {data.decode()}")

            # Send response back to client
            conn.sendall("Hello from server!".encode())

    except socket.error as error:
        print(f"Socket error: {error}")

    finally:
        # Clean disconnection process
        try:
            conn.close()
            print("Connection closed cleanly.")
        except:
            pass

        server.close()
        print("Server socket closed cleanly.")

if __name__ == "__main__":
    main()

