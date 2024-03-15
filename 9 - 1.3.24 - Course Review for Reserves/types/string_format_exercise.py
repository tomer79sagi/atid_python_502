my_str = 'Awad'
my_age = 45

line = "Hi, my name is {}, and I'm {} years old".format(my_str, my_age)
line2 = "Hi, my name is {1}, and I'm {0} years old".format(my_str, my_age)
line3 = "Hi, my name is {my_name}, and I'm {age} years old".format(my_name='Tomer', age=45)
line4 = f"Hi, my name is {my_str}, and I'm {my_age} years old"

print(line)
print(line2)
print(line3)
print(line4)