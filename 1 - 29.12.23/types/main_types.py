myInput = input("Please enter your age ")
print(type(myInput))  # Prints the type of the variable 'myInput'

# Define my age - 5 years
youngerAge = int(myInput) - 5  # Cast the 'str' variable 'myInput' to 'int'
print(youngerAge)  # 40

# Divide youngerAge by 2
ageBy2 = int(myInput) / 2
print(type(ageBy2))  # int / int --> (if required) float
print(int(youngerAge / 2))  # / (division) --> float
