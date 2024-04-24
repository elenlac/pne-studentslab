import json
import termcolor
from pathlib import Path

# -- Read the json file
jsonstring = Path("people-2.json").read_text()

# Create the object person from the json string
person = json.loads(jsonstring)
# Person is now a DICTIONARY.

# Read the values associated to the fields(KEYS): 'Firstname', 'Lastname' and 'age' and directly print (no variables)
print()
termcolor.cprint("Name: ", 'green', end="")
print(person['Firstname'], person['Lastname'])
termcolor.cprint("Age: ", 'green', end="")
print(person['Age'])

"""DIFFERENCE FROM TEST-JSON-1"""
# Get the phoneNumber list of str
phoneNumbers = person['PhoneNumbers']

# Print the NUMBER(int) OF ELEMENTS/PHONE NUMBERS in the list
termcolor.cprint("Phone numbers: ", 'green', end='')
print(len(phoneNumbers))

# Print all the phone numbers
for i, num in enumerate(phoneNumbers):  # ["1111", "2222"] -> [(0, "1111"), (1, "2222")]
    termcolor.cprint("  Phone " + str(i) + ": ", 'blue', end='')
    print(num)
# enumerate = iterator that produces a sequence of tuples, each containing an index and the value from the iterable
# the enumerate object is returned in a key-value pair format. Key=corresponding index of each item & value=the items
