from Seq0 import *
print("-----| Exercise 7 |------")

g = "U5"
n = 20

folder = "../sequences/"
filename = g + ".txt.fa"
file = folder + filename
sequence = seq_read_fasta(file)
fragment = sequence[:n]

print(f"Gene {str(g)}:\nFrag: {fragment}\nComp: {seq_complement(fragment)}")