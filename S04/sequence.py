from pathlib import Path

filename = "sequences/ADA.txt.fa"
file_contents = Path(filename).read_text()

lines = file_contents.split("\n")
lines.pop(0)

length = 0
for line in lines:
    s = line.replace("\n", "")
    length += len(s)

print("Total length:", length)

