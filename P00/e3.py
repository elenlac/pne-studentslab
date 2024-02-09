from Seq0 import *
print("-----| Exercise 3 |------")

genes = ["U5", "ADA", "FRAT1", "FXN"]  # list with the names of the Genes
for g in genes:  # for loop for iterating over the 4 genes and calculating their lengths
    folder = "../sequences/"
    filename = g + ".txt.fa"  # filename can be obtained by adding the ".txt.fa" string to the gene name
    file = folder + filename
    sequence = seq_read_fasta(file)

    print("Gene", g, "->", "Length:", seq_len(sequence))
