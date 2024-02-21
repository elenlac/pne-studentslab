"""This file is our module, that will be imported in all the exercises"""


class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases=None):
        bases_list = ["A", "C", "T", "G"]
        s = ""
        if strbases is None or strbases == "":
            self.strbases = "NULL"
            print("NULL sequence created")
        else:
            for b in strbases:
                if b in bases_list:
                    self.strbases = strbases
                    s += b
            if len(s) == len(strbases):
                print("New sequence created!")
            else:
                self.strbases = "ERROR"
                print("INVALID sequence!")



    def __str__(self):
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        if self.strbases == "NULL" or self.strbases == "ERROR":
            length = 0
        else:
            length = len(self.strbases)
        return length

    def count_base(self, base):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            count = 0
        else:
            count = self.strbases.count(base)
        return count

    def count(self):
        bases_dict = {"A": 0, "T": 0, "C": 0, "G": 0}

        if self.strbases == "NULL" or self.strbases == "ERROR":
            return bases_dict
        else:
            for b in self.strbases:
                bases_dict[b] += 1
            return bases_dict



