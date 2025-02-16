"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

"""
is_finished = false
while not is_finished
    try
        get result as integer
        is_finished = true
    catch invalid number error
        print "Please enter a valid integer."

print "Valid result is:", result

"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)
