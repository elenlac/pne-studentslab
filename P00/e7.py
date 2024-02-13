from Seq0 import *
print("-----| Exercise 7 |------")

g = "U5"

# fist we find the file
folder = "../sequences/"
filename = g + ".txt.fa"
file = folder + filename
sequence = seq_read_fasta(file)  # we apply this function for the sequence to be in one line
sequence = sequence[:20]
complement = seq_complement(sequence)  # we apply our new function

print("Gene", str(g) + ":", "\n", "Frag" + ":", sequence, "\n", "Comp" + ":", complement)