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
    count = seq.count(base)
    return count

# EXERCISE 5


def seq_count(seq):
    bases_dict = {"A": 0, "T": 0, "C": 0, "G": 0}  # empty dictionary that will store the basis

    for b in seq:  # b represents each different base (key) in our dictionary
        bases_dict[b] += 1  # adds values to each base

    return bases_dict

# EXERCISE 6


def seq_reverse(seq, n):
    n_sequence = seq[:n]
    reverse = n_sequence[::-1]  # iterable[start:end:step]]
    # step is negative so iterable is run backwards, and default values when start and end are omitted are inverted
    return reverse

# EXERCISE 7


def seq_complement(seq):
    complements_dict = {"A": "T", "T": "A", "C": "G", "G": "C"}
    complementary_seq = ""

    for b in seq:
        complementary_seq += complements_dict[b]
    #  for each iteration of the loop, it takes the current base, looks up its complementary base
    #  in the dict, and appends it to the complementary_seq string

    return complementary_seq

# EXERCISE 8


def max_base(seq):
    bases_dict = {"A": 0, "T": 0, "C": 0, "G": 0}  # empty dictionary that will store the basis

    for b in seq:  # b represents each different base (key) in our dictionary
        bases_dict[b] += 1  # adds values to each base

    most_frequent_base = max(bases_dict, key=bases_dict.get)
    # the maximum is determined based on the values in the dictionary, but the key is the one returned

    return most_frequent_base
