# Display all odd numbers between 1 and 20, each separated by a space
for i in range(1, 21, 2):
    print(i, end=' ')
print()


# a. Count in 10s from 0 to 100
"""
<Pseudocode:>
for i from 0 to 100 step 10
        print i on the same line
    print newline
"""
for i in range(0, 101, 10):
    print(i, end=' ')
print()


# b. Count down from 20 to 1
"""
<Pseudocode:>
    for i from 20 to 1 step -1
        print i on the same line
    print newline
"""
for i in range(20, 0, -1):
    print(i, end=' ')
print()


# c. Print n stars on one line
"""
<Pseudocode:>
get n as integer
    for i from 0 to n - 1
        print '*' on the same line
    print newline
"""
n = int(input("Number of stars: "))
for i in range(n):
    print('*', end='')
print()


# d. Print n lines of increasing stars
"""
<Pseudocode:>
for i from 1 to n
    print '*' repeated i times
"""
for i in range(1, n + 1):
    print('*' * i)

