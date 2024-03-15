def sum_and_avg(num1, num2, num3):
    my_sum = num1 + num2 + num3
    my_avg = my_sum / 3

    return my_sum, my_avg


s, a = sum_and_avg(1, 5, 99)

print(f"The Sum is: {s}\nThe Average is: {a}")


# function that returns a LIST object (similar to Java's Array)
def get_student_list():
    return ['Tomer', 'Awad', 'Oded']  # List of 3 students

# function that returns a DICTIONARY object (similar to Java's HashMap / HashTable)
def get_student_dict():
    return {'student_1': 'Tomer', 'student_2': 'Awad', 'student_3': 'Oded'}

# function that returns a SET object
# Set doesn't allow Duplicates, and is unordered
def get_student_set():
    return {'Tomer', 'Awad', 'Oded', 3}

# function that returns a TUPLE object
# Can't grow or shrink the structure
# Can change the values in the tuple
def get_student_tuple():
    return ('Tomer', 'Awad', 'Oded')


# s1, s2, s3 = get_student_list()

my_set = get_student_set()
s1, s2, s3, s4 = get_student_set()