from Seq0 import *
print("-----| Exercise 5 |------")

genes = ["U5", "ADA", "FRAT1", "FXN"]
for g in genes:
    folder = "../sequences/"
    filename = g + ".txt.fa"
    file = folder + filename
    sequence = seq_read_fasta(file)
    bases_dict = seq_count(sequence)

    print(f"Gene {str(g)}: {bases_dict}")
