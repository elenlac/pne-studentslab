from Seq0 import *
print("-----| Exercise 5 |------")

folder = "../sequences/"
for gene_name in ["U5", "ADA", "FRAT1", "FXN"]:
    filename = (gene_name + ".txt.fa")
    file = folder + filename
    seq_len(file)
