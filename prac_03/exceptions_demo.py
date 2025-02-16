"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A ValueError occurs when the user inputs a value that cannot be converted into an integer. For example, if the user enters a string that isn't a number,
 such as "abc", it will raise a ValueError because int("abc") is not a valid conversion.

2. When will a ZeroDivisionError occur?
A ZeroDivisionError occurs when the user tries to divide a number by zero.
This happens if the denominator entered by the user is 0, as division by zero is mathematically undefined.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, in order to avoid the possibility of ZeroDivisionError,
I can add a check before performing division to ensure that the denominator is not zero.
"""

"""
try
    get numerator as integer
    get denominator as integer

    if denominator is 0
        print "Cannot divide by zero!"
    else
        fraction = numerator / denominator
        print fraction

catch invalid number error
    print "Numerator and denominator must be valid numbers!"

print "Finished."

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    # Check if the denominator is zero before performing division
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")
