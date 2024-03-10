from Seq0 import *
folder = "../sequences/"  # with the 2 dots the program goes outside P00 and looks for the sequences folder
filename = "U5.txt.fa"
sequence = seq_read_fasta(folder + filename)

""" ANOTHER WAY TO DO IT THAT WORKS FOR ANY OPERATIVE SYSTEM
import os
filename = os.path.join("..", "sequences", GENE + ".txt.fa")
"""

print("DNA file:", filename)
print(f"The first 20 bases are:\n{sequence[:20]}")

