from seq_01 import Seq


def generate_seqs(pattern, number):  # will create a list with the provided number of sequences(pattern)
    new_sequences = []  # here we store the new sequences created each iteration
    for i in range(1, number + 1):  # start in 1 (we would be returning an empty list in 0)
        sequence = Seq(pattern * i)  # the current sequence(pattern) will be repeated a determined number of times (i)
        new_sequences.append(sequence)  # we append the sequence, that we turned into and object, to our list
    return new_sequences

# we needed to turn our sequence into an object (with Seq) in order to be able to apply these following functions:


def print_seqs(seq_list):  # like the one from e2 but with a different version of the code (using ENUMERATE)
    for i, seq in enumerate(seq_list):
        print(f"Sequence {i}: (Length: {seq.len()}) {seq}")


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1)

print()
print("List 2:")
print_seqs(seq_list2)
