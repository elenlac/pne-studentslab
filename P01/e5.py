from Seq1 import Seq

practice = 1
exercise = 5

print(f"-----| Practice {practice} , Exercise {exercise} |------")

seq_list = [Seq(), Seq("ACTGA"), Seq("Invalid sequence")]
for i, seq in enumerate(seq_list):
      print(f"Sequence {i + 1}: (Length: {seq.len()}) {seq} \n A: {seq.count_base('A')},  C: {seq.count_base('C')},  "
            f"T: {seq.count_base('T')},  G: {seq.count_base('G')}")


""" 
# the problem with this loop is that we don't use the commas
for b in Seq.bases_list:
    print(f"\t{b}: {seq.count_base(b)}, end="" ")  # we use the end in order to put everything in one line
    print()
    """
