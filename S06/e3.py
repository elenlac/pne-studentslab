class Seq:
    def __init__(self, sequence):
        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.sequence = sequence

    def __str__(self):
        return self.sequence

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.sequence)


def print_seqs(seq_list):
    for seq in seq_list:
        index = seq_list.index(seq)
        length = seq.len()
        sequence = seq
        print(f"Sequence {index}: (Length: {length}) {sequence}")


def generate_seqs(pattern, number):  # will create a list with the provided number of sequences
    result = pattern * number

    return result


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1)

print()
print("List 2:")
print_seqs(seq_list2)
