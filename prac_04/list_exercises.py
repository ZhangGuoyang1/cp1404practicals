"""
function main()
    initialize empty list numbers
    for i from 1 to 5
        get number from user
        add number to numbers list

    print the first number in numbers
    print the last number in numbers
    print the smallest number in numbers
    print the largest number in numbers
    print the average of the numbers (sum of numbers divided by length of numbers)

    initialize list usernames with authorized usernames
    get username from user
    if username is in usernames
        print "Access granted"
    else
        print "Access denied"

"""

# Part 1: Prompt the user for 5 numbers and store them in a list
numbers = []
for i in range(5):
    number = float(input("Number: "))
    numbers.append(number)

# Output information about the numbers
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

# Part 2: Check if the user is authorized
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
             'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
             'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

# Ask the user for their username
username = input("Enter your username: ")

# Check if the username is in the list of authorized users
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
