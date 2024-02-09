from Seq0 import *
print("-----| Exercise 5 |------")

genes = ["U5", "ADA", "FRAT1", "FXN"]  # list with the names of the Genes
bases = ["A", "C", "T", "G"]  # list with the names of the bases

for g in genes:  # for loop for iterating over the 4 genes

    # fist we find the files
    folder = "../sequences/"
    filename = g + ".txt.fa"
    file = folder + filename
    sequence = seq_read_fasta(file)  # we apply this function for the sequence to be in one line

    print("Gene", str(g) + ":")  # inside this loop to print the proper gene name once (not for every base count)

    for b in bases:  # for loop for iterating over the 4 bases that we can find in each gene
        base_count = seq_count_base(sequence, b)  # we apply our new function
        print(" ", b + ":", base_count)  # inside this loop ensuring it prints the counts for each base
