import os
from Seq2 import Seq
from Client0 import Client

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

    msg = f"Sending FRAT1 Gene to the server, in fragments of 10 bases..."
    reponse0 = c.talk(msg)

    fragment = str(s)[:10]
    fragment1 = f"Fragment 1: {fragment}"
    print(fragment1)
    response1 = c.talk(fragment1)


except FileNotFoundError:
    print(f"[ERROR]: file '{filename}' not found")
