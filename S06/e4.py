import termcolor


class Seq:
    def __init__(self, sequence):
        self.sequence = sequence

    def __str__(self):
        return self.sequence

    def len(self):
        return len(self.sequence)


def generate_seqs(pattern, number):  # will create a list with the provided number of sequences(pattern)
    new_sequences = []  # here we store the new sequences created each iteration
    for i in range(1, number + 1):  # we start in 1 since we would be returning an empty list in 0
        sequence = pattern * i  # the current sequence(pattern) will be repeated a determined number of times (i)
        new_sequences.append(Seq(sequence))  # we append the sequence to our list
        print("New sequence created!")
    return new_sequences


def print_seqs(seq_list, color):
    for seq in seq_list:
        index = seq_list.index(seq)
        length = seq.len()
        termcolor.cprint(f"Sequence {index}: (Length: {length}) {seq}", color)


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

termcolor.cprint("List 1:", "blue")
print_seqs(seq_list1, "blue")

print()
termcolor.cprint("List 2:", "green")
print_seqs(seq_list2, "green")
