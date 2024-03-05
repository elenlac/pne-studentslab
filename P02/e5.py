import os
from Seq2 import Seq
from Client0 import Client
from termcolor import *

practice = 2
exercise = 5

print(f"-----| Practice {practice}, Exercise {exercise} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8081

# -- Create a client object
c = Client(IP, PORT)

# -- Create a Null sequence
s = Seq()

try:
    filename = os.path.join("..", "sequences", "FRAT1" + ".txt.fa")
    s.read_fasta(filename)

    print(f"Gene FRAT1: {s}")

    msg = colored(f"Sending FRAT1 Gene to the server, in fragments of 10 bases...", "green")
    response0 = c.talk(msg)

    start = 0
    end = 10
    for i in range(5):  # it repeats 5 times
        f = str(s)[start:end]
        start += 10
        end += 10
        fragment = colored(f"Fragment {i+1}: {f}", "green")
        print(fragment)
        response1 = c.talk(fragment)


except FileNotFoundError:
    print(f"[ERROR]: file '{filename}' not found")
