def valid_bases(strbases):
    valid = True
    for b in strbases:
        if b not in Seq.bases_list:  # the Seq in front indicates that bases_list is a class attribute
            valid = False
            break  # you exit the for loop
    return valid


class Seq:
    bases_list = ["A", "C", "T", "G"]  # list with the bases of a DNA sequence (class attribute or property or static)

    def __init__(self, strbases):
        if valid_bases(strbases):
            self.strbases = strbases
            print("New sequence created!")
        else:
            self.strbases = "ERROR"
            print("INCORRECT Sequence detected")

    def __str__(self):
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)


class Gene(Seq):
    """This class is derived from the Seq Class
       All the objects of class Gene will inherit
       the methods from the Seq class
    """
    def __init__(self, strbases, name=""):

        # -- Call first the Seq initializer and then the
        # -- Gene init method
        super().__init__(strbases)
        self.name = name
        print("New gene created")

    def __str__(self):
        """Print the Gene name along with the sequence"""
        return self.name + "-" + self.strbases


"""
# Main program
# Create objects of the class Seq
s1 = Seq("AGTACACTGGT")
g = Gene("CGTAAC", "FRAT1")
s2 = Seq("CGTAAC")


# -- Printing the objects
print(f"Sequence 1: {s1}")
print(f"Gene: {g}")
print(f"  Length: {s1.len()}")  # s1.len() Execute the action for calculating the length on the s1 object
print(f"Sequence 2: {s2}")
print(f"  Length: {s2.len()}")"""