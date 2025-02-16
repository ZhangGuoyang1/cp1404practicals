"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""


"""
DEFINE MIN_LENGTH = 2
DEFINE MAX_LENGTH = 6
DEFINE IS_SPECIAL_CHARACTER_REQUIRED = false
DEFINE SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\"

function main()
    print "Please enter a valid password"
    print "Your password must be between " + MIN_LENGTH + " and " + MAX_LENGTH + " characters, and contain:"
    print "    1 or more uppercase characters"
    print "    1 or more lowercase characters"
    print "    1 or more numbers"
    
    if IS_SPECIAL_CHARACTER_REQUIRED
        print "    and 1 or more special characters: " + SPECIAL_CHARACTERS

    get password

    while not is_valid_password(password)
        print "Invalid password!"
        get password

    print "Your " + length of password + " character password is valid: " + password

function is_valid_password(password)
    if length of password < MIN_LENGTH or length of password > MAX_LENGTH
        return false

    SET number_of_lower = 0
    SET number_of_upper = 0
    SET number_of_digit = 0
    SET number_of_special = 0

    for each character in password
        if character is lowercase
            number_of_lower += 1
        else if character is uppercase
            number_of_upper += 1
        else if character is digit
            number_of_digit += 1
        else if character is in SPECIAL_CHARACTERS
            number_of_special += 1

    if number_of_lower == 0 or number_of_upper == 0 or number_of_digit == 0
        return false
        
    if IS_SPECIAL_CHARACTER_REQUIRED and number_of_special == 0
        return false

    return true

"""
MIN_LENGTH = 2
MAX_LENGTH = 6
IS_SPECIAL_CHARACTER_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if IS_SPECIAL_CHARACTER_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)

    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)} character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""

    # Check length of the password
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    number_of_lower = 0
    number_of_upper = 0
    number_of_digit = 0
    number_of_special = 0

    for character in password:
        if character.islower():
            number_of_lower += 1
        elif character.isupper():
            number_of_upper += 1
        elif character.isdigit():
            number_of_digit += 1
        elif character in SPECIAL_CHARACTERS:
            number_of_special += 1

    # Check if all required character types are present
    if number_of_lower == 0 or number_of_upper == 0 or number_of_digit == 0:
        return False

    # If special characters are required, check that there is at least one
    if IS_SPECIAL_CHARACTER_REQUIRED and number_of_special == 0:
        return False

    # If we passed all checks, the password is valid
    return True


main()

