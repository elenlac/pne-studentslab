import os
from Seq2 import Seq
from Client0 import Client
from termcolor import *

practice = 2
exercise = 6
number_of_bases = 10

print(f"-----| Practice {practice}, Exercise {exercise} |------")

# -- Parameters of the servers to talk to
IP = "127.0.0.1"
PORT1 = 8080
PORT2 = 8081

# -- Create two client objects
c1 = Client(IP, PORT1)
print(c1)
c2 = Client(IP, PORT2)
print(c2)


filename = os.path.join("..", "sequences", "FRAT1" + ".txt.fa")
try:
    # -- Create a Null sequence
    s = Seq()

    s.read_fasta(filename)

    print(f"Gene FRAT1: {s}")

    msg = colored(f"Sending FRAT1 Gene to the server, in fragments of {number_of_bases} bases...", "green")
    reponse1 = c1.talk(msg)
    response2 = c2.talk(msg)

    start = 0
    end = number_of_bases
    number_fragments = 10
    s_str = str(s)

    for i in range(1, number_fragments + 1):
        f = s_str[start:end]
        msg = colored(f"Fragment {i}: {f}", "green")
        print(msg)

        if i % 2 == 0:  # if the number is even then we operate in the server2
            response2 = c2.talk(msg)

        else:  # if the number is odd then we operate in the server1
            response1 = c1.talk(msg)

        start += number_fragments
        end += number_fragments


except FileNotFoundError:
    print(f"[ERROR]: file '{filename}' not found")
