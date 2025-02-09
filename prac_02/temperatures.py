"""
<Pseudocode:>

function celsius_to_fahrenheit(celsius)
    return celsius * 9.0 / 5 + 32

function fahrenheit_to_celsius(fahrenheit)
    return 5 / 9 * (fahrenheit - 32)

MENU = "C - Convert Celsius to Fahrenheit
        F - Convert Fahrenheit to Celsius
        Q - Quit"

print MENU
get choice
choice = choice in uppercase

while choice is not "Q"
    if choice is "C"
        get celsius
        fahrenheit = celsius_to_fahrenheit(celsius)
        print "Result:", fahrenheit, "F"
    else if choice is "F"
        get fahrenheit
        celsius = fahrenheit_to_celsius(fahrenheit)
        print "Result:", celsius, "C"
    else
        print "Invalid option"

    print MENU
    get choice
    choice = choice in uppercase

print "Thank you."

"""

def celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)


MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()

while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"Result: {celsius:.2f} C")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()

print("Thank you.")
