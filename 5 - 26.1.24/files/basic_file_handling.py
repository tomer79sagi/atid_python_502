# [A] READING FROM FILES
file = open('data.csv', 'r')

# (1) 'read()' method
# contents = file.read()
# print(contents)

# (2) readline() method
# single_line = file.readline()
# print(single_line)

# (3) readlines() method - multiple lines
# single_line = file.readlines()
# print(single_line)

# (4) Loop over file lines
for line in file:
    print(line)


# [B] WRITING TO A FILE
# (1) 'write'
w_file = open('example.txt', 'w')
w_file.write('Hi, my name is Tomer Sagi')


# [B] APPENDING TO A FILE
# (1) 'write'
w_file = open('example.txt', 'a')  # APPEND
w_file.write('\nThis is a wonderful day')

# MUST always close a file in the end
w_file.close()


# [C] AUTO-CLOSE FILES AT THE END
# This will automatically run the 'close()' method in the end
# We don't have to add it ourselves
with open('example.txt', 'a') as file:
    file.write('\nThis is a third line')