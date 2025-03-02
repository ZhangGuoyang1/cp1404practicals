"""
Word Occurrences
Estimate: 20 minutes
Actual:   25 minutes
"""

"""
function main()
    create dictionary key_to_value to store email (key) and name (value)

    while true
        prompt user for email input
        if email is blank
            break the loop

        extract name from email using extract_name_from_email function

        ask user if the extracted name is correct
        if user confirms (empty or 'y')
            store email and name in key_to_value dictionary
        else
            ask user for the correct name and store it in key_to_value

    for each email, name pair in key_to_value
        print the name and email in the format "Name (email)"

function extract_name_from_email(email)
    split email at '@' and get the part before '@'
    replace any dots in the name part with spaces
    capitalize each word in the name part
    return formatted name

if program is run as main
    call main function



"""

def main():
    key_to_value = {}  # Dictionary to store emails (keys) and names (values)

    while True:
        # Ask for an email input
        email = input("Email: ")
        if email == "":
            break  # Exit loop if email is blank

        # Extract a name from the email
        name = extract_name_from_email(email)

        # Ask the user if the name is correct
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirmation == '' or confirmation == 'y':
            # If yes or default (Y), store the email and name in the dictionary
            key_to_value[email] = name
        else:
            # If no, ask for the correct name
            name = input("Name: ")
            key_to_value[email] = name

    # Loop through the dictionary and print out the emails and names
    for email, name in key_to_value.items():
        print(f"{name} ({email})")

def extract_name_from_email(email):
    # Extract the part before '@' and capitalize it
    name_part = email.split('@')[0]
    # Replace any dots in the name part with spaces and capitalize each word
    return ' '.join(name_part.split('.')).title()

if __name__ == "__main__":
    main()
