from seq_01 import Seq
import termcolor


def generate_seqs(pattern, number):
    new_sequences = []
    for i in range(1, number + 1):
        sequence = Seq(pattern * i)
        new_sequences.append(sequence)
    return new_sequences


def print_seqs(seq_list, color):  # we add this new parameter to indicate the color we want to paint it with
    for i, seq in enumerate(seq_list):
        termcolor.cprint(f"Sequence {i}: (Length: {seq.len()}) {seq}", color)


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

termcolor.cprint("List 1:", "blue")
print_seqs(seq_list1, "blue")

print()
termcolor.cprint("List 2:", "green")
print_seqs(seq_list2, "green")
