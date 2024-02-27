import os
from Seq1 import Seq
practice = 1
exercise = 10

print(f"-----| Practice {practice} , Exercise {exercise} |------")

genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]


for g in genes:
    filename = os.path.join("..", "sequences", g + ".txt.fa")
    try:
        s = Seq()
        s.read_fasta(filename)  # -- Initialize the null seq with the given file in fasta format
        print(f"Gene {g}: Most frequent Base: {s.max_base()}")
    except FileNotFoundError:
        print(f"[ERROR]: file '{filename}' not found")


#  update