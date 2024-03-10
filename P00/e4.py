from Seq0 import *
print("-----| Exercise 4 |------")

genes = ["U5", "ADA", "FRAT1", "FXN"]
bases = ["A", "C", "T", "G"]

for g in genes:
    folder = "../sequences/"
    filename = g + ".txt.fa"
    file = folder + filename
    sequence = seq_read_fasta(file)

    print(f"Gene {str(g)}:")  # inside THIS loop to print the gene name once (not for every base count)

    for b in bases:  # for loop for iterating over the 4 bases that we can find in each gene
        base_count = seq_count_base(sequence, b)
        print(f"\b {b}: {base_count}")  # inside THIS loop ensuring it prints the counts for each base
    print("\n")
