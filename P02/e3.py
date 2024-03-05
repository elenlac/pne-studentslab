from Client0 import Client

practice = 2
exercise = 3

print(f"-----| Practice {practice}, Exercise {exercise} |------")

# -- Parameters of the server to talk to
IP = "192.168.1.41"  # your IP address
PORT = 8081

# -- Create a client object
c = Client(IP, PORT)

# -- Send a message to the server
print("Sending a message to the server...")
response = c.talk("Testing!!!")
print(f"Response:\n")
print(f"{response}")
