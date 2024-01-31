#  a mechanism to open the file that does not require calling to close function for it to be closed is "with()"
with open("dna.txt", "r") as f:
    for line in f:
        s = line.replace("\n", "")  # in order to eliminate the "\n" at the end of each line
        length = len(s)
        bases_dict = {"A": 0, "C": 0, "G": 0, "T": 0}  # empty dictionary that will store the basis
        for b in s:  # b represents each different base (key) in our dictionary
            bases_dict[b] += 1  # adds values to each base

        print("Total length:", length, bases_dict)

