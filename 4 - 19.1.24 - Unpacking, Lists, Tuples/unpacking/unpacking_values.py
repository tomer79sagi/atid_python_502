def my_sum(*integers):
    result = 0
    for i in integers:
        result += i

    print(result)


my_sum(1, 2, 3, 4, 6, 7, 8)
