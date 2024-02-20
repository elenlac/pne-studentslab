class Seq:
    def __init__(self, sequence):
        self.sequence = sequence

    def __str__(self):
        return self.sequence

    def len(self):
        return len(self.sequence)


def print_seqs(seq_list):  # seq_list represents any list containing sequences that belong to the Seq class
    for seq in seq_list:  # seq represents each of the individual sequences of seq_list
        index = seq_list.index(seq)  # we use this variable to determine where is our sequence located in the list
        length = seq.len()  # now we calculate the length of such sequence with the previous function
        print(f"Sequence {index}: (Length: {length}) {seq}")


seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print_seqs(seq_list)



