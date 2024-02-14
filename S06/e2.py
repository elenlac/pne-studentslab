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


seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print_seqs(seq_list)



