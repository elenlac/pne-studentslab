import socket

# Configure the Server's IP and PORT
PORT = 8080
IP = "127.0.0.1"  # this IP address is local, so only requests from the same machine are possible

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

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listening socket
        listening_socket.close()

        # -- Exit!, it first exits the infinite loop and then terminates the whole program
        exit()

    # -- Execute this part if there are no errors, it the exception KeyboardInterrupt is not executed
    else:

        print("A client has connected to the server!")

        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_bytes = client_socket.recv(2048)

        # -- We decode it for converting it
        # -- into a human-readable string
        msg = msg_bytes.decode()

        # -- Print the received message
        print(f"Message received: {msg}")

        # -- Send a response message to the client
        response = "HELLO. I am the Happy Server :-)\n"

        # -- The message has to be encoded into bytes
        client_socket.send(response.encode())  # works as str.encode(response)

        # -- Close the data socket
        client_socket.close()
