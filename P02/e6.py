import os
from Seq2 import Seq
from Client0 import Client
from termcolor import *

practice = 2
exercise = 6

print(f"-----| Practice {practice}, Exercise {exercise} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT1 = 8080
PORT2 = 8081

# -- Create a client object
c1 = Client(IP, PORT1)
c2 = Client(IP, PORT2)


filename = os.path.join("..", "sequences", "FRAT1" + ".txt.fa")
try:
    # -- Create a Null sequence
    s = Seq()

    s.read_fasta(filename)

    print(f"Gene FRAT1: {s}")

    msg = colored(f"Sending FRAT1 Gene to the server, in fragments of 10 bases...", "green")
    reponse1 = c1.talk(msg)
    response2 = c2.talk(msg)

    start = 0
    end = 10
    for i in range(10):
        if i % 2 == 0:  # if the number is even then we operate in the server2
            f = str(s)[start:end]
            start += 10
            end += 10
            fragment = colored(f"Fragment {i+1}: {f}", "green")
            print(fragment)
            response = c2.talk(fragment)
        elif i % 2 != 0:  # if the number is odd then we operate in the server1
            f = str(s)[start:end]
            start += 10
            end += 10
            fragment = colored(f"Fragment {i+1}: {f}", "green")
            print(fragment)
            response = c1.talk(fragment)


except FileNotFoundError:
    print(f"[ERROR]: file '{filename}' not found")
