from Seq1 import Seq

print("-----| Practice 1, Exercise 5 |------")

# -- Null sequence
s0 = Seq()

# -- Valid sequence
s1 = Seq("ACTGA")

# -- Invalid sequence
s2 = Seq("Invalid sequence")

print(f"Sequence 0: (Length: {s0.len()}) {s0} \n A: {s0.count_base('A')},  C: {s0.count_base('C')},"
      f"  T: {s0.count_base('T')},  G: {s0.count_base('G')} ")
print(f"Sequence 1: (Length: {s1.len()}) {s1} \n A: {s1.count_base('A')},  C: {s1.count_base('C')},"
      f"  T: {s1.count_base('T')},  G: {s1.count_base('G')} ")
print(f"Sequence 2: (Length: {s2.len()}) {s2} \n A: {s2.count_base('A')},  C: {s2.count_base('C')},"
      f"  T: {s2.count_base('T')},  G: {s2.count_base('G')} ")
