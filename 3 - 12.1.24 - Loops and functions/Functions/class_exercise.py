def math_calc(a, b, c, d, e):
    s = a + b + c + d + e
    avg = s / 5

    my_list = [a, b, c, d, e]
    current_min = a  # 30 in our example
    for element in my_list:
        if current_min > element:
            current_min = element

    return s, avg, current_min


my_sum, my_avg, my_min = math_calc(30, 88, 22, 44, 5)
print(my_sum, my_avg, my_min)
