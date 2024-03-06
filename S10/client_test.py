from Client0 import Client
from termcolor import *

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8082

# -- Create a client object
c = Client(IP, PORT)

# -- Send a message to the server
for i in range(5):
    msg = colored(f"Message {i}", "blue")
    print(f"To Server: {msg}")

    msg2 = colored(f"Message {i}", "green")
    response = c.talk(msg)
    print(colored(f"From Server: ECHO: {msg2}\n", "green"))
