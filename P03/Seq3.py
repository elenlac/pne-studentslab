"""This file is our module, that will be imported in all the exercises"""
"""It is a copy of the Seq 1 file from practice 1"""


def valid_bases(strbases):
    valid = True
    for b in strbases:
        if b not in Seq.bases_list:  # the Seq in front indicates that bases_list is a class attribute
            valid = False
            break  # you exit the for loop
    return valid


class Seq:
    bases_list = ["A", "C", "T", "G"]  # list with the bases of a DNA sequence (class attribute or property or static)

    def __init__(self, strbases=None):
        if strbases is None or len(strbases) == 0:  # the same as strbases == 0
            self.strbases = "NULL"
            print("NULL sequence created")
        elif valid_bases(strbases):
            self.strbases = strbases
            print("New sequence created!")
        else:
            self.strbases = "ERROR"
            print("INVALID sequence!")

    def __str__(self):
        return self.strbases

    def len(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            length = 0
            # return 0
            # return len(self.strbases)
        else:
            length = len(self.strbases)
        return length

    def count_base(self, base):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            count = 0
            # return 0
            # return self.strbases.count(base)
        else:
            count = self.strbases.count(base)
        return count

    def count(self):  # as we use count_base, in this function we don't need to check if the sequence is valid
        bases_dict = {}

        for b in Seq.bases_list:  # b acting as each one of the bases of our list of valid bases(class property)
            bases_dict[b] = self.count_base(b)  # the value of each one of the keys(b) will be their individual count
        return bases_dict

    def reverse(self):
        if self.strbases == "NULL":
            reverse = "NULL"
        elif self.strbases == "ERROR":
            reverse = "ERROR"
        else:
            reverse = self.strbases[::-1]
        return reverse

    def complement(self):
        complements_dict = {"A": "T", "T": "A", "C": "G", "G": "C"}
        complementary_seq = ""

        if self.strbases == "NULL":
            complementary_seq = "NULL"
        elif self.strbases == "ERROR":
            complementary_seq = "ERROR"
        else:
            for b in self.strbases:
                complementary_seq += complements_dict[b]
        return complementary_seq

    def read_fasta(self, filename):
        from pathlib import Path

        file_content = Path(filename).read_text()
        lines = file_content.splitlines()
        body = lines[1:]

        dna_sequence = ""
        for line in body:
            dna_sequence += line  # dna_sequence = dna_sequence + line
        self.strbases = dna_sequence

    def max_base(self):
        bases_dict = {}
        for b in Seq.bases_list:
            bases_dict[b] = self.count_base(b)

        most_frequent_base = max(bases_dict, key=bases_dict.get)
        # the maximum is determined based on the values in the dictionary, but the key is the one returned

        return most_frequent_base

