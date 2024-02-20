class Seq:
    def __init__(self, sequence):
        bases_list = ["A", "C", "T", "G"]  # list with the valid bases of a DNA sequence
        s = ""  # empty string where valid sequences will be stored
        for b in sequence:  # b representing base
            if b in bases_list:  # checks if such base is in the bases_list
                self.sequence = sequence  # sets self.sequence to the input sequence
                s += b  # if it does belong to the list, it is appended to the empty string s creating a valid sequence
        if len(s) == len(sequence):  # for a last check-up, it sees if the length of s matches the original length
            print("New sequence created!")  # meaning that all characters in the input sequence are valid bases
        else:  # if lengths don't match, invalid character(s) found, it returns a message
            self.sequence = "ERROR"  # sequence initialized with the "ERROR" string
            print("INCORRECT Sequence detected")

    def __str__(self):
        return self.sequence

# two instances of the Seq class are created, and it prints the string representation of each using the __str__ method


s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")

