class Seq:
    def __init__(self, sequence):
        bases_list = ["A", "C", "T", "G"]
        s = ""
        for b in sequence:
            if b in bases_list:
                self.sequence = sequence
                s += b
        if len(s) == len(sequence):
            print("New sequence created!")
        else:
            self.sequence = "ERROR"
            print("ERROR!!")

    def __str__(self):
        return self.sequence


s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")

