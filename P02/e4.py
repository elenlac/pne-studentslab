import os
from Seq2 import Seq
from Client0 import Client

practice = 2
exercise = 4

print(f"-----| Practice {practice}, Exercise {exercise} |------")

# -- Parameters of the server to talk to
IP = "192.168.1.41"
PORT = 8081

# -- Create a client object
c = Client(IP, PORT)

# -- Create a Null sequence
s = Seq()

genes = ["U5", "ADA", "FRAT1", "FXN"]
try:
    for g in genes:  # for loop for iterating over the 4 genes and calculating their lengths
        filename = os.path.join("..", "sequences", g + ".txt.fa")
        s.read_fasta(filename)  # -- Initialize the null seq with the given file in fasta format
    # -- Send a message to the server
    print(f"To Server: Sending the U5 Gene to the server...")
    response = c.talk("Testing!!!")
    print(f"From Server:\n")
    print(f"{response}\n")
    print(f"To Server: {s}")

except FileNotFoundError:
    print(f"[ERROR]: file '{filename}' not found")



