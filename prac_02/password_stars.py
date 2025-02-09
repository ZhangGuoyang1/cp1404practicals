"""
min_length = 8

password = input("Enter your password: ")
while len(password) < min_length:
    print(f"Password must be at least {min_length} characters long.")
    password = input("Enter your password: ")
print("*" * len(password))

"""


"""
<Pseudocode:>

function get_password(min_length)
    get password from user
    while length of password < min_length
        print "Password must be at least {min_length} characters long."
        get password from user
    return password

function print_asterisks(password)
    print "*" repeated for length of password

function main()
    set min_length to 8
    password = get_password(min_length)
    print_asterisks(password)

"""

def get_password(min_length):
    password = input("Enter your password: ")

    while len(password) < min_length:
        print(f"Password must be at least {min_length} characters long.")
        password = input("Enter your password: ")

    return password


def print_asterisks(password):
    print("*" * len(password))


def main():
    min_length = 8
    password = get_password(min_length)
    print_asterisks(password)


if __name__ == "__main__":
    main()
