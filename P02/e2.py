from Client0 import Client

practice = 2
exercise = 2

print(f"-----| Practice {practice}, Exercise {exercise} |------")

# -- Parameters of the server to talk to
IP = "212.128.255.83"  # your IP address
PORT = 8081

# -- Create a client object
c = Client(IP, PORT)

# -- Test the str method
print(c)
