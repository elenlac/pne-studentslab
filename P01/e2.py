from Seq1 import Seq

practice = 1
exercise = 2

print(f"-----| Practice {practice} , Exercise {exercise} |------")

"""We will manage three types of sequences: Valid, Invalid and Null:
- Null: Empty sequence "". It has no bases at all"""

seq_list = [Seq(), Seq("ACTGA")]
for i, seq in enumerate(seq_list):
    print(f"Sequence {i+1}: {seq}")  # +1 because it starts on 0 by default
