from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "sequences/RNU6_269P.txt.fa"  # it is important to put the folder name before with a slash to indicate where the file is located and open it

# -- Open and read the file
file_contents = Path(FILENAME).read_text()

# -- Print the contents on the console
print(file_contents)
