import json
import termcolor
from pathlib import Path

# -- Read the json file
jsonstring = Path("people-3.json").read_text()

# Create the object person from the json string
person = json.loads(jsonstring)
# Person is now a DICTIONARY.

# Read the values associated to the fields(KEYS): 'Firstname', 'Lastname' and 'age' and directly print (no variables)
print()
termcolor.cprint("Name: ", 'green', end="")
print(person['Firstname'], person['Lastname'])
termcolor.cprint("Age: ", 'green', end="")
print(person['age'])

# Get the phoneNumber list
phoneNumbers = person['phoneNumber']

# Print the number of elements in the list
termcolor.cprint("Phone numbers: ", 'green', end='')
print(len(phoneNumbers))

"""DIFFERENCE FROM TEST-JSON-2"""
# Print all the numbers
for i, dictnum in enumerate(phoneNumbers):
    termcolor.cprint("  Phone " + str(i + 1) + ": ", 'blue')

    # The element num contains 2 fields: number and type
    termcolor.cprint("\t- Type: ", 'red', end='')
    print(dictnum['type'])
    termcolor.cprint("\t- Number: ", 'red', end='')
    print(dictnum['number'])
