"""
function main()
    data = load_data()
    call display_subject_details with data as parameter

function load_data()
    initialize empty list data
    open FILENAME for reading and store in input_file
    for each line in input_file
        strip newline from line
        split line by comma into parts
        convert parts[2] to integer (number of students)
        add parts to data list
    close input_file
    return data

function display_subject_details(data)
    for each subject in data
        unpack subject into subject_code, lecturer, student_count
        print subject_code, lecturer, and student_count in formatted string


"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subject_details(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []  # Create an empty list to store the data
    input_file = open(FILENAME)

    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number of students an integer
        data.append(parts)  # Add the list of parts to the data list

    input_file.close()
    return data  # Return the data as a list of lists


def display_subject_details(data):
    """Display details for each subject in the data list."""
    for subject in data:
        subject_code, lecturer, student_count = subject
        print(f"{subject_code} is taught by {lecturer:12} and has {student_count:3} students")


main()
