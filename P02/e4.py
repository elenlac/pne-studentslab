import os
from Seq2 import Seq
from Client0 import Client
from termcolor import *

practice = 2
exercise = 4

print(f"-----| Practice {practice}, Exercise {exercise} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8081

# -- Create a client object
c = Client(IP, PORT)

# -- Create a Null sequence
s = Seq()

genes = ["U5", "FRAT1", "ADA"]
try:
    for g in genes:
        filename = os.path.join("..", "sequences", g + ".txt.fa")
        s.read_fasta(filename)  # -- Initialize the null seq with the given file in fasta format

        # -- Send a message to the server
        msg = colored(f"Sending the {g} Gene to the server...", "blue")
        print(f"To Server: {msg}")

        print(f"From Server:\n")
        response = colored(c.talk(msg), "green")
        print(f"{response}\n")

        str_sequence = str(s)
        msg2 = colored(str_sequence, "blue")
        print(f"To Server: {msg2}")
        response = colored(c.talk(msg2), "green")
        print(f"{response}\n")


except FileNotFoundError:
    print(f"[ERROR]: file '{filename}' not found")



