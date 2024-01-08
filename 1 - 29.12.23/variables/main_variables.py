# This is a comment
# 'int' type example
myVar = 5
myVar = 5 + 7
print(myVar)

# 'float' type example
myFloat = 4.5  # Automatically converts to type 'float'
print(myFloat)

# 'bool' type example
# myBool = True
myBool = 5 == 7
print(myBool)

# 'str' type example
myStr = "Hello, I'm a teacher"
myStr2 = 'Hello, this my "Corvette"'
print(myStr, myStr2)

# 'str' as array
myStr3 = "I'm teaching Python at Atid College"
print(myStr3[4])  # t
print(myStr3[-1])  # e
print(myStr3[-4])  # l

# 'str' with slicing
myStr4 = "I'm teaching Python at Atid College"
print(myStr4[2:10])  # m teachin
print(myStr4[2:10:2])  # mtah

# 'str' functions
myStr5 = "I'm teaching Python at Atid College"
print('myStr5',len(myStr5))
print(myStr5.upper())
print(myStr5.find('Python'))  # 13

# 'str' - format, merge variables inside a string
myStr5 = 'Tomer'
myAge = 45
myMergedStr = "My name {0}, my age is {1}".format(myStr5, myAge)
print(myMergedStr)
