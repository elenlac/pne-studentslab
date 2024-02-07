from Seq0 import *
sequence = seq_read_fasta("../sequences/U5.txt.fa")
# with the 2 dots the program goes outside P00 and looks for the sequences folder
print(sequence[:21])
