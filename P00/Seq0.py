# Common file where we find all the functions that we need
def seq_ping():
    print("OK")

def seq_read_fasta(filename):
    from pathlib import Path
    file_contents = Path(filename).read_text()

    lines = file_contents.split("\n")
    lines.pop(0)

    s = ""
    for line in lines:
        s += line
    return s

def seq_len(seq):
    sequence = seq_read_fasta(seq)
    length = len(sequence)
    print("Length:", length)

def seq_count_base(seq, base):
    sequence = seq_read_fasta(seq)
    bases = ["A", "C", "G", "T"]
    for base in sequence:







