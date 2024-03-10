from Seq0 import *
print("-----| Exercise 8 |------")

genes = ["U5", "ADA", "FRAT1", "FXN"]

for g in genes:
    folder = "../sequences/"
    filename = g + ".txt.fa"
    file = folder + filename
    sequence = seq_read_fasta(file)

    fashion = most_frequent_base(sequence)

    print(f"Gene {str(g)}: Most frequent Base: {fashion}")
