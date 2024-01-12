def fun():
    d = dict()

    d['string'] = "This is a fun string"
    d['age'] = 43

    return d  # 'dictionary' data type (similar to HashMap or Hashtable in Java)


my_dict = fun()
print(my_dict['string'])
print(my_dict['age'])
