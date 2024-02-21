from Seq0 import *
folder = "../sequences/"  # with the 2 dots the program goes outside P00 and looks for the sequences folder
filename = "U5.txt.fa"
sequence = seq_read_fasta(folder + filename)

print("DNA file:", filename)
print("The first 20 bases are:", sequence[:20])

