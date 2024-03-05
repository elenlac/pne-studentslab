import socket

# SERVER IP, PORT
PORT = 8081
IP = "127.0.0.1"  # it depends on the machine the server is running


clientsocket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket2.connect((IP, PORT))

clientsocket2.send(str.encode("HELLO FROM THE CLIENT!!!"))

# Receive data from the server
msg = clientsocket2.recv(2048).decode("utf-8")
print(f"Message from server: {msg}")

clientsocket2.close()
