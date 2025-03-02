"""
define code_to_name as a dictionary with state abbreviations and full names
    "qld" -> "queensland"
    "nsw" -> "new south wales"
    "nt" -> "northern territory"
    "wa" -> "western australia"
    "act" -> "australian capital territory"
    "vic" -> "victoria"
    "tas" -> "tasmania"
    "sa" -> "south australia"

print code_to_name

for each state_code, state_name in code_to_name
    print state_code, "is", state_name

get state_code from user input and convert to uppercase
while state_code is not blank
    try
        print state_code, "is", code_to_name[state_code]
    catch keyerror
        print "invalid short state"

    get state_code from user input and convert to uppercase



"""


# Dictionary to store the state codes and names
CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia"
}
print(CODE_TO_NAME)

# Loop to print all states and names in formatted output
for state_code, state_name in CODE_TO_NAME.items():
    print(f"{state_code} is {state_name}")

# Function to handle user input for state abbreviation
state_code = input("Enter short state: ").upper()  # Convert input to uppercase
while state_code != "":
    try:
        # Try to get the full name using the state code
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    except KeyError:
        # Handle invalid state codes
        print("Invalid short state")

    # Prompt the user again for input
    state_code = input("Enter short state: ").upper()  # Convert input to uppercase
