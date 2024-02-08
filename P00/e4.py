from Seq0 import *
print("-----| Exercise 4 |------")

genes = ["U5", "ADA", "FRAT1", "FXN"]  # list with the names of the Genes
bases = ["A", "C", "G", "T"]
list_of_lists = []
for g in genes:  # for loop for iterating over the 4 genes and calculating their lengths
    base_count = []
    for b in bases:
        base_count.append(seq_count_base(g, b))
    list_of_lists.append(base_count)

print(list_of_lists)
