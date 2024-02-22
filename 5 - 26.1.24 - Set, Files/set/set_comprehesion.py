list_1 = [1, 2, 3, 10]
list_2 = range(10)

print(list_1)
print(list_2)

# list Comprehension
# list_3 = [expression for item in iterable if condition]
list_3 = ['Tomer_' + str(i) for i in list_2 if i % 2 == 0]
print(list_3)


# set comprehension
set_1 = {'{} - Tomer'.format(str(i)) for i in list_1 if i % 2 != 0}  # '{}' --> set()
# set_1 = {f'{str(i)} - Tomer' for i in list_1 if i % 2 != 0}  # '{}' --> set()
print(set_1)


# dictionary comprehension
# {key_expression: value_expression for item in iterable if condition}
# This line takes a 'set' and returns a 'dictionary' from it
dict_1 = {str(element): f'{str(element)} Sagi' for element in set_1}
print(dict_1)
