# Question 1: Ask for user name, write it to "name.txt" using open and close
"""
get name
open "name.txt" as file for writing
write name to file
close file

"""

name = input("Enter your name: ")
file = open('name.txt', 'w')
file.write(name)
file.close()

# Question 2: Open "name.txt", read the name, and print a greeting using open and close
"""
open "name.txt" as file for reading
read name_from_file from file
close file

remove extra whitespace from name_from_file
print "Hi " + name_from_file + "!"

"""
file = open('name.txt', 'r')
name_from_file = file.read().strip()  # strip to remove any extra whitespace
file.close()
print(f"Hi {name_from_file}!")

# Question 3: Read the first two numbers from "numbers.txt", add them and print the result
# Create the "numbers.txt" first and save it with the numbers 17, 42, 400 on separate lines

"""
open "numbers.txt" as file for reading
read all lines from file into numbers
close file

convert numbers[0] to integer and remove extra whitespace
convert numbers[1] to integer and remove extra whitespace
SET sum_of_first_two = numbers[0] + numbers[1]

print sum_of_first_two

"""
with open('numbers.txt', 'r') as file:
    numbers = file.readlines()
    sum_of_first_two = int(numbers[0].strip()) + int(numbers[1].strip())  # convert to int and add
    print(sum_of_first_two)  # Output: 59

# Question 4: Print the total sum of all the numbers in "numbers.txt"
"""
open "numbers.txt" as file for reading

SET total = 0

for each line in file
    convert line to integer and remove extra whitespace
    total = total + line

close file

print total

"""
with open('numbers.txt', 'r') as file:
    total = 0
    for line in file:
        total += int(line.strip())  # Add each line's number to the total
    print(total)  # This will print the sum of all numbers in the file
