import os
from Seq2 import Seq
from Client0 import Client
from termcolor import *

practice = 2
exercise = 5
number_of_bases = 10

print(f"-----| Practice {practice}, Exercise {exercise} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8081

# -- Create a client object
c = Client(IP, PORT)

# -- Test the str method
print(c)

g = "FRAT1"
filename = os.path.join("..", "sequences", g + ".txt.fa")
try:
    # -- Create a Null sequence
    s = Seq()

    s.read_fasta(filename)
    print(f"Gene {g}: {s}")

    msg = colored(f"Sending {g} Gene to the server, in fragments of {number_of_bases} bases...", "green")
    response = c.talk(msg)

    start = 0
    end = number_of_bases
    number_fragments = 5
    s_str = str(s)

    for i in range(number_fragments):  # it repeats 5 times in this case, goes from 0 to number of fragments
        fragment = s_str[start:end]  # we first call the str method, then we slice the sequence [0:9]
        msg = colored(f"Fragment {i+1}: {fragment}", "green")
        print(msg)
        response = c.talk(msg)

        start += number_of_bases
        end += number_of_bases

    """
    for i in range(1, number_fragments + 1):
        print(f"Fragment {i}: {f}")
    """


except FileNotFoundError:
    print(f"[ERROR]: file '{filename}' not found")


