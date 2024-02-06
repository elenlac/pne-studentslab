from pathlib import Path

filename = "sequences/RNU6_269P.txt.fa"
file_contents = Path(filename).read_text()
print(file_contents)

lines = file_contents.split("\n")

print(lines[0])  # the first line is the header
