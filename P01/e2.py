from Seq1 import Seq

practice = 1
exercise = 2

print(f"-----| Practice {practice} , Exercise {exercise} |------")

seq_list = [Seq(), Seq("TATAC")]  # creating a NULL and VALID sequence
for i, seq in enumerate(seq_list):  # creates a new list of tuples such that: [(0,s1), (1, s2)]
    print(f"Sequence {i+1}: {seq}")  # +1 because it starts on 0 by default
