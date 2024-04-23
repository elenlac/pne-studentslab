import json
import termcolor
from pathlib import Path

# -- Read the json file AND BECOMES A STR
jsonstring = Path("people-1.json").read_text()

# Create the OBJECT person from the json string
person = json.loads(jsonstring)
# Person is now a DICTIONARY.

# We can read the values associated to the fields(KEYS): 'Firstname', 'Lastname' and 'age'
firstname = person['Firstname']
lastname = person['Lastname']
age = person['age']

# Print the information on the console, in colors
print()
termcolor.cprint("Name: ", 'green', end="")
print(firstname, lastname)
termcolor.cprint("Age: ", 'green', end="")
print(age)
