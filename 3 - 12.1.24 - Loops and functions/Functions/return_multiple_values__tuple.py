def fun():
    my_str = "This is a fun string"
    x = 43
    return my_str, x, 56, 'Have a good day'  # 'tuple' data type
    # return (my_str, x) # Also 'tuple' data type


s, y, a, b = fun()
print(s, y)
print(a, b)
