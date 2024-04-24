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
print(person['Age'])

# Get the phoneNumber list of dicts
phoneNumbers = person['PhoneNumbers']

# Print the number of elements in the list (2 dictionaries in this case)
termcolor.cprint("Phone numbers: ", 'green', end='')
print(len(phoneNumbers))

"""DIFFERENCE FROM TEST-JSON-2"""
# Print all the numbers
for i, dictnum in enumerate(phoneNumbers):  # we are enumerating a list of DICTS(dictnum), not a list of STR(num)
    termcolor.cprint("  Phone " + str(i + 1) + ": ", 'blue')

    # The element num contains 2 fields: number and type
    termcolor.cprint("\t- Type: ", 'red', end='')
    print(dictnum['type'])  # we treat the variable dictum as a dict
    termcolor.cprint("\t- Number: ", 'red', end='')
    print(dictnum['number'])
