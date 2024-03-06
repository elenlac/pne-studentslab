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

# -- Test the str method
print(c)

g = "FRAT1"
filename = os.path.join("..", "sequences", g + ".txt.fa")
try:
    # -- Create a Null sequence
    s = Seq()

    s.read_fasta(filename)

    print(f"Gene {g}: {s}")

    msg = colored(f"Sending {g} Gene to the server, in fragments of 10 bases...", "green")
    response = c.talk(msg)

    start = 0
    end = 10
    number_fragments = 5
    for i in range(number_fragments):  # it repeats 5 times in this case, goes from 0 to number of fragments
        f = str(s)[start:end]
        start += 10
        end += 10
        fragment = colored(f"Fragment {i+1}: {f}", "green")
        print(fragment)
        response1 = c.talk(fragment)

    """
    number_fragments = 5
    number_bases = 10 
    
    for i in range(1, number_fragments + 1):
        print(f"Fragment {i+1}: {f}")
    
    
    """


except FileNotFoundError:
    print(f"[ERROR]: file '{filename}' not found")


# update