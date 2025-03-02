"""
function main()
    create dictionary COLOR_NAMES with color names and their hexadecimal codes

    print instructions for user to enter color name or stop with blank line

    get color_name from user input, strip whitespace, convert to lowercase

    while color_name is not blank
        format color_name to title case

        try
            if formatted_color_name is in COLOR_NAMES
                print the hexadecimal code for formatted_color_name
        catch KeyError
            print "Invalid color name"

        get color_name from user input again, strip whitespace, convert to lowercase


"""



# Constant dictionary of color names and their corresponding hexadecimal codes
COLOR_NAMES = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "Blue": "#0000ff"
}

# Print instructions for the user
print("Enter a color name (e.g., AliceBlue) to get its hexadecimal code.")
print("Enter a blank line to stop the program.")

# Loop to get user input and display the corresponding color code
color_name = input("Enter color name: ").strip().lower()  # Convert input to lowercase for case-insensitivity
while color_name != "":
    # Convert input to proper case (title case) to match dictionary keys
    formatted_color_name = color_name.title()

    try:
        # Try to find the color name in the dictionary and print the corresponding code
        print(f"The hexadecimal code for {formatted_color_name} is {COLOR_NAMES[formatted_color_name]}")
    except KeyError:
        # Handle invalid color names
        print("Invalid color name")

    # Prompt the user again for input
    color_name = input("Enter color name: ").strip().lower()  # Convert input to lowercase for case-insensitivity
