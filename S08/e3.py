import socket

# SERVER IP, PORT
PORT = 8081
IP = "212.128.255.75"


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((IP, PORT))

message = input("Enter a message: ")
s.send(str.encode(message))

s.close()

