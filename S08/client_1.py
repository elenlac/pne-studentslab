import socket

# Write here the correct parameter for connecting to the Teacher's server
SERVER_PORT = 8081  # it is the port that our client will connect to
SERVER_IP = "127.0.0.1"  # it is the ip that our client will connect to


# First, create the socket. We will always use these parameters: AF_INET y SOCK_STREAM
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# establish the connection to the Server (IP, PORT)
clientsocket.connect((SERVER_IP, SERVER_PORT))
# it establishes "the name of the client tunnel"(bind), opens such "tunnel"(listen) and connects to the server "tunnel"
# connect() has a direct connexion with accept() since when it is executed accept() continues

# Send data. No strings can be sent, only bytes. It necessary to encode the string into bytes.
clientsocket.send(str.encode("HELLO FROM THE CLIENT!!!"))   # send() has direct connexion with recv()

# Close the socket, the "tunnel"
clientsocket.close()

