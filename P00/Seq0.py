# Common file where we find all the functions that we need

# EXERCISE 1


def seq_ping():
    print("OK")

# EXERCISE 2


def seq_read_fasta(filename):  # useful for the sequence to be in one line
    from pathlib import Path
    file_contents = Path(filename).read_text()

    lines = file_contents.split("\n")
    lines.pop(0)

    s = ""
    for line in lines:
        s += line
    return s

# EXERCISE 3


def seq_len(seq):
    length = len(seq)
    return length


# EXERCISE 4


def seq_count_base(seq, base):
    sequence = seq_read_fasta(seq)
    bases = ["A", "C", "G", "T"]
    genes = ["U5", "ADA", "FRAT1", "FXN"]
    for g in genes:
        for b in bases:
            filename = "sequences" + g + ".txt"

# EXERCISE 5


def seq_count(seq):
    bases_dict = {"A": 0, "C": 0, "G": 0, "T": 0}  # empty dictionary that will store the basis

    sequence = seq_read_fasta(seq)
    for b in sequence:  # b represents each different base (key) in our dictionary
        bases_dict[b] += 1  # adds values to each base

    print(bases_dict)

# update