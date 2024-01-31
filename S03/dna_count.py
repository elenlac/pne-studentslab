
sequence = input("Introduce the sequence:")
length = len(sequence)
bases_dict = {"A": 0, "C": 0, "G": 0, "T": 0}  # empty dictionary that will store the basis
for b in sequence:  # b represents each different base (key) in our dictionary
    bases_dict[b] += 1  # adds values to each base

print("Total length:", length, bases_dict)



