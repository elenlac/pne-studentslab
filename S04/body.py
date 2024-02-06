from pathlib import Path

filename = "sequences/U5.txt.fa"
file_contents = Path(filename).read_text()

lines = file_contents.split("\n")

for i in range(1, len(lines)):  # you skip the O, which is the header line
    print(lines[i])  # you print each line
