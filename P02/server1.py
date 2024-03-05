import socket

# Configure the Server's IP and PORT

PORT = 8080
IP = "127.0.0.1"  # it depends on the machine the server is running, here the IP is 127.0.0.1
MAX_OPEN_REQUESTS = 5

number_con = 0

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    serversocket.bind((IP, PORT))

    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections

    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        print(f"Waiting for connections at {IP}, {PORT}")
        (clientsocket, address) = serversocket.accept()

        # Another connection!e
        number_con += 1

        # Print the connection number
        print(f"CONNECTION: {number_con}. From the address: {address}")

        # Read the message from the client, if any

        msg = clientsocket.recv(2048).decode("utf-8")
        print(f"Message from client: {msg}")

        # Send the message
        clientsocket.send(str.encode("Hello from the server\n"))

        clientsocket.close()

except socket.error:
    print(f"Problems using ip {IP} port {PORT}. Is the IP correct? Do you have port permission?")

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()

