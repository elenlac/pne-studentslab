from Seq1 import Seq

practice = 1
exercise = 2

print(f"-----| Practice {practice} , Exercise {exercise} |------")

seq_list = [Seq(), Seq("TATAC")]
for i, seq in enumerate(seq_list):
    print(f"Sequence {i+1}: {seq}")

