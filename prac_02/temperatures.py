"""
CP1404/CP5632 - Practical

<Pseudocode for temperature conversion>
constant MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit"

print MENU
get choice as uppercase input
while choice is not "Q"
    if choice is "C"
        get celsius as float
        fahrenheit = celsius * 9.0 / 5 + 32
        print "Result:", fahrenheit formatted to 2 decimal places, "F"
    elif choice is "F"
        get fahrenheit as float
        celsius = 5 / 9 * (fahrenheit - 32)
        print "Result:", celsius formatted to 2 decimal places, "C"
    else
        print "Invalid option"
    print MENU
    get choice as uppercase input
print "Thank you."

"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print(f"Result: {celsius:.2f} C")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")