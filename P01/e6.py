from Seq1 import Seq

practice = 1
exercise = 6

print(f"-----| Practice {practice} , Exercise {exercise} |------")

seq_list = [Seq(), Seq("ACTGA"), Seq("Invalid sequence")]
for i, seq in enumerate(seq_list):
    print(f"Sequence {i}: (Length: {seq.len()}) {seq}\n Bases: {seq.count()}")
