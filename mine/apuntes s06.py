# 27/02/24

"""para que funcione el termcolor module:
PS C:\Users\elena\PycharmProjects\pne-studentslab> CD S06
PS C:\Users\elena\PycharmProjects\pne-studentslab\S06> python test-color.py
Hey! this is printed in green!
PS C:\Users\elena\PycharmProjects\pne-studentslab\S06>"""


# VERSIÓN ANTERIOR DE E1
class Seq:
    bases_list1 = ["A", "C", "T", "G"]  # list with the valid bases of a DNA sequence

    def __init__(self, sequence):
        s = ""  # empty string where valid sequences will be stored
        for b in sequence:  # b representing base
            bases_list = ["A", "C", "T", "G"]  # list with the valid bases of a DNA sequence
            if b in bases_list:  # checks if such base is in the bases_list
                self.sequence = sequence  # sets self.sequence to the input sequence
                s += b  # if it does belong to the list, it is appended to the empty string s creating a valid sequence
        if len(s) == len(sequence):  # for a last check-up, it sees if the length of s matches the original length
            print("New sequence created!")  # meaning that all characters in the input sequence are valid bases
        else:  # if lengths don't match, invalid character(s) found, it returns a message
            self.sequence = "ERROR"  # sequence initialized with the "ERROR" string
            print("INCORRECT Sequence detected")


# OTRA FORMA DE HACERLO CON EL RETURN
    def __init__(self, strbases):
        for b in strbases:  # b represents each base in the sequence
            if b not in Seq.bases_list1:  # checks if such base is not in the bases_list1
                self.strbases = "ERROR"  # in strbases we store "ERROR"
                print("INCORRECT Sequence detected")
                return  # you exit the for loop and the function
        self.strbases = strbases
        print("New sequence created!")
