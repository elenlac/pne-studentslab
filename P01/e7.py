from Seq1 import Seq

print("-----| Practice 1, Exercise 7 |------")

# -- Null sequence
s0 = Seq()

# -- Valid sequence
s1 = Seq("ACTGA")

# -- Invalid sequence
s2 = Seq("Invalid sequence")

print(f"Sequence 0: (Length: {s0.len()}) {s0} \n Bases: {s0.count()} \n Rev: {s0.reverse()}")
print(f"Sequence 1: (Length: {s1.len()}) {s1} \n Bases: {s1.count()} \n Rev: {s1.reverse()}")
print(f"Sequence 2: (Length: {s2.len()}) {s2} \n Bases: {s2.count()} \n Rev: {s2.reverse()}")