from Client0 import Client
from termcolor import *

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8082

# -- Create a client object
c = Client(IP, PORT)

# -- Send a message to the server
for i in range(5):
    message = f"Message {i}"
    msg_blue = colored(f"Message {i}", "blue")
    print(f"To Server: {msg_blue}")
    response = c.talk(message)

    msg_green = colored(f"ECHO: {message}", "green")
    print(f"From Server: {msg_green}\n")
