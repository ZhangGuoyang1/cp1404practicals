
MIN_LENGTH = 8
password = input("Please enter a password (minimum length 8): ")
while len(password) < MIN_LENGTH:
    print(f"Password must be at least {MIN_LENGTH} characters long.")
    password = input("Please enter a password (minimum length 8): ")
print('*' * len(password))
