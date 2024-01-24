def my_sum(**words):
    result = 0
    for i in words.values():
        result += i
    print(result)


my_sum(grade_1=44, grade_2=65, grade_3=88, grade_4=99)
