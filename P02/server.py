import socket

# Configure the Server's IP and PORT (they are in mayus since they act as constants)

PORT = 8081
IP = "127.0.0.1"  # it depends on the machine the server is running, here the IP is 127.0.0.1
MAX_OPEN_REQUESTS = 5

number_con = 0  # this is a variable that counts how many connections are to the server, it can increase or decrease

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# first socket = module, and the second = class (you are calling the init from the class socket and create an object)
# AF_INET: class attribute (constant), determines that socket acts over the IP protocol
# SOCK_STREAM: class attribute (constant) I am going to receive and send bytes (streaming: data flow)

try:
    serversocket.bind((IP, PORT))  # we are asking our object to link to the duple (double tuple) named as ENDPOINT

    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections

    serversocket.listen(MAX_OPEN_REQUESTS)  # listen allows clients to connect the server, "the tunnel is opened"
    # plus, only 5 clients will be listened/connected to the server at the same time

    while True:  # infinite loop that accepts connections from outside, from clients
        print(f"Waiting for connections at {IP}, {PORT}")
        (clientsocket, address) = serversocket.accept()
        # accept allows the socket accept the connexion of a socket,
        # it is a blocking instruction: until it is executed, my code does not follow. It is waiting for a client.
        # accept gives tuple with clientsocket for server to know HOW to connect to it and the address of client.

        # Another connection!e
        number_con += 1

        # Print the connection number
        print(f"CONNECTION: {number_con}. From the address: {address}")  # address= ip_client + port_client

        # Read the message from the client, if any

        msg = clientsocket.recv(2048).decode("utf-8")
        # 2048 the max amount of bytes received (blocking instruction)
        # and with decode we transform the bites received to str (utf-8 is a text format)
        print(f"Message from client: {msg}")

        # Send the message
        clientsocket.send(str.encode("Hello from the server\n"))

        clientsocket.close()

except socket.error:
    print(f"Problems using ip {IP} port {PORT}. Is the IP correct? Do you have port permission?")

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()

