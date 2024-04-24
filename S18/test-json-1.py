import json  # provides tools to work with json format
import termcolor
from pathlib import Path

# -- Open and read the json file AND BECOMES A STR
jsonstring = Path("people-1.json").read_text()

# Create the OBJECT person from the json string
person = json.loads(jsonstring)  # using the module json, we use the method to load the content and traduce into a dict
# Person is now a DICTIONARY.

# We can read the values associated to the fields(KEYS): 'Firstname', 'Lastname' and 'Age'
firstname = person['Firstname']
lastname = person['Lastname']
age = person['Age']

# Print the information on the console, in colors
print()
termcolor.cprint("Name: ", 'green', end="")
print(firstname, lastname)
termcolor.cprint("Age: ", 'green', end="")
print(age)
