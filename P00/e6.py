from Seq0 import *
print("-----| Exercise 6 |------")

g = "U5"

# fist we find the file
folder = "../sequences/"
filename = g + ".txt.fa"
file = folder + filename
sequence = seq_read_fasta(file)  # we apply this function for the sequence to be in one line

reverse = seq_reverse(sequence, 20)  # we apply our new function

print("Gene", str(g), "\n", "Fragment" + ":", sequence[:20], "\n", "Reverse" + ":", reverse)