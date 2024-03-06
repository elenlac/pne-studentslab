import socket
from termcolor import *

"""An echo server is a server that responds with the same message sent by the client."""

# Configure the Server's IP and PORT
PORT = 8082
IP = "127.0.0.1"  # this IP address is local, so only requests from the same machine are possible
number_con = 0
list_clients = []

# -- Step 1: create the socket: LISTENING SOCKET = SERVER SOCKET
listening_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
listening_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
listening_socket.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
listening_socket.listen()

print("The server is configured!")


while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")

    try:
        (client_socket, client_ip_port) = listening_socket.accept()
        number_con += 1
        print(f"CONNECTION: {number_con}. Client IP, PORT: {client_ip_port}")  # address= ip_client + port_client

        list_clients.append(client_ip_port)

    # -- Server stopped manually
    except KeyboardInterrupt:

        print("Server stopped by the user")

        # -- Close the listening socket
        listening_socket.close()

        # -- Exit!
        exit()

    # -- Execute this part if there are no errors
    else:

        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_bytes = client_socket.recv(2048)

        # -- We decode it for converting it
        # -- into a human-readable string
        msg = colored(msg_bytes.decode(), "green")

        # -- Print the received message
        print(f"Message received: {msg}")

        # -- Send a response message to the client
        response = f"ECHO: {msg}\n"

        # -- The message has to be encoded into bytes
        client_socket.send(response.encode())

        if number_con == 5:
            print(f"The following clients have connected to the server:")

            for i in range(5):
                print(f"Client {i}: {list_clients[i]}")

            # -- Close the data socket
            client_socket.close()

            # -- Exit!
            exit()
