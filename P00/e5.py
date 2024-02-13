from Seq0 import *
print("-----| Exercise 5 |------")

genes = ["U5", "ADA", "FRAT1", "FXN"]  # list with the names of the Genes

for g in genes:  # for loop for iterating over the 4 genes

    # fist we find the files
    folder = "../sequences/"
    filename = g + ".txt.fa"
    file = folder + filename
    sequence = seq_read_fasta(file)  # we apply this function for the sequence to be in one line
    bases_dict = seq_count(sequence)  # we apply our new function

    print("Gene", str(g) + ":", bases_dict)
