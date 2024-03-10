from Seq1 import Seq

practice = 1
exercise = 5

print(f"-----| Practice {practice} , Exercise {exercise} |------")

seq_list = [Seq(), Seq("ACTGA"), Seq("Invalid sequence")]
for i, seq in enumerate(seq_list):
      print(f"Sequence {i}: (Length: {seq.len()}) {seq} \n A: {seq.count_base('A')},  C: {seq.count_base('C')},  "
            f"T: {seq.count_base('T')},  G: {seq.count_base('G')}")


""" ANOTHER WAY, BUT HERE WE DON'T USE THE COMMAS:
for b in Seq.bases_list:
    print(f"\t{b}: {seq.count_base(b)}, end="" ") 
    # print function ends with a newline by default, end="" indicates that there is NO end character.
    """
