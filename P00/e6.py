from Seq0 import *
print("-----| Exercise 6 |------")

g = "U5"  # as we only have one gene, we don't need to do a for loop
n = 20

folder = "../sequences/"
filename = g + ".txt.fa"
file = folder + filename
sequence = seq_read_fasta(file)

print(f"Gene {str(g)}\nFragment: {sequence[:n]}\nReverse: {seq_reverse(sequence, n)}")
