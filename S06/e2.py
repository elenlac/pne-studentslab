from seq_01 import Seq


def print_seqs(seq_list):  # seq_list represents any list containing sequences that belong to the Seq class
    for seq in seq_list:  # seq represents each of the individual sequences of seq_list
        index = seq_list.index(seq)  # we use index function to ask our list(=object) where is each seq located in it
        length = seq.len()  # now we calculate the length of such sequence with the previous len function
        print(f"Sequence {index}: (Length: {length}) {seq}")


seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print_seqs(seq_list)



