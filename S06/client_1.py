import socket

# SERVER IP, PORT
# Write here the correct parameter for connecting to the
# Teacher's server
PORT = 8081
IP = "212.128.255.64"  # it depends on the machine the server is running


# First, create the socket
# We will always use these parameters: AF_INET (internet socket=understands IP protocol) y SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT): tuple that is why two pair of brackets appear
s.connect((IP, PORT))  # if there is no server you will get an error

# Send data. No strings can be sent, only bytes
# It necessary to encode the string into bytes
s.send(str.encode("HELLO FROM THE CLIENT!!!"))  # transform the string into bytes

# Close the socket
s.close()
# update
