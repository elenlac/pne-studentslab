import os
from Seq1 import Seq
print("-----| Practice 1, Exercise 9 |------")

# -- Create a Null sequence
s = Seq()


GENE = "U5"

filename = os.path.join("..", "sequences", GENE + ".txt.fa")
try:
    s = s.read_fasta(filename)  # -- Initialize the null seq with the given file in fasta format
    print(f"Sequence: (Length: {s.len()}) {s} \n Bases: {s.count()} \n Rev: {s.reverse()} \n Comp: {s.complement()}")
except FileNotFoundError:
    print(f"[ERROR]: file '{filename}' not found")
