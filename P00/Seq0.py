"""This file is our module, that will be imported in all the exercises"""


# EXERCISE 1: FUNCTION USED JUST FOR TESTING
def seq_ping():  # by default, all functions return None
    print("OK")


# EXERCISE 2: OPENS A FILE IN FASTA FORMAT AND RETURNS A STRING WITH THE DNA SEQUENCE
def seq_read_fasta(filename):
    from pathlib import Path  # pathlib is a module and Path is a class

    file_content = Path(filename).read_text()  # creates a Path object and the following method reads the file
    lines = file_content.splitlines()  # this method splits a string into a list of substrings, using \n as separator
    body = lines[1:]  # body also acts as a list, but we remove the header

    dna_sequence = ""  # for each iteration, it will become larger
    for line in body:  # for each loop, line acts as a different element(line) of the body(list)
        dna_sequence += line  # dna_sequence = dna_sequence + line

    return dna_sequence  # we have turned our list into a single str


# EXERCISE 3: CALCULATES THE TOTAL NUMBER OF BASES IN A SEQUENCE
def seq_len(seq=None):
    length = len(seq)
    return length


# EXERCISE 4: CALCULATES THE NUMBER OF TIMES THAT A GIVEN BASE APPEARS IN THE SEQUENCE
def seq_count_base(seq, base=None):
    count = seq.count(base)
    return count


# EXERCISE 5:
def seq_count(seq):  # CALCULATES THE NUMBER OF TIMES THAT A GIVEN BASE APPEARS IN THE SEQUENCE IN A DICTIONARY
    bases = ["A", "C", "T", "G"]
    bases_appearances = {}
    for b in bases:  # for each turn, we create a new key-value relationship that we add to the dictionary
        bases_appearances[b] = seq_count_base(seq, b)  # DICT: key(b)-value(number of appearances using count_base)
    return bases_appearances


""" ANOTHER WAY TO DO IT, BUT ALREADY ESTABLISHING OUR KEYS
bases_dict = {"A": 0, "T": 0, "C": 0, "G": 0}  # empty dictionary that will store the basis
for b in seq:  # b represents each different base (key) in our dictionary
    bases_dict[b] += 1  # adds values to each base
return bases_dict
"""


# EXERCISE 6: CALCULATES THE REVERSE OF FIRST N BASES OF A GIVEN SEQUENCE
def seq_reverse(seq, n):
    n_sequence = seq[:n]  # we "slice" the sequence according to the given number of bases (n)
    reverse = n_sequence[::-1]  # iterable[start:end:step]
    # STEP is negative, so the iterable is run backwards, and default values when start and end are omitted are inverted

    return reverse


# EXERCISE 7: CALCULATES A NEW SEQ COMPOSED OF THE COMPLEMENT BASE OF EACH OF THE ORIGINAL BASES
def seq_complement(seq):
    complements_dict = {"A": "T", "T": "A", "C": "G", "G": "C"}
    complementary_seq = ""

    for b in seq:
        complementary_seq += complements_dict[b]
    #  for each iteration of the loop, it takes the current base, looks up its complementary base in the dict,
    #  and appends it to the complementary_seq string

    return complementary_seq


# EXERCISE 8: CALCULATES THE MOST FREQUENT BASE IN EACH GENE
def most_frequent_base(seq):
    bases = ["A", "C", "T", "G"]
    max_base = ""
    max_count = 0
    for base in bases:
        count = seq_count_base(seq, base)
        if count > max_count:
            max_count = count
            max_base = base
    return max_base


""" ANOTHER WAY TO DO IT
bases_dict = {"A": 0, "T": 0, "C": 0, "G": 0}  # empty dictionary that will store the basis
for b in seq:  # b represents each different base (key) in our dictionary
    bases_dict[b] += 1  # adds values to each base

    most_frequent_base = max(bases_dict, key=bases_dict.get)
    # the maximum is determined based on the values in the dictionary, but the key is the one returned

    return most_frequent_base
"""
