# Mutable
fruits = ["apple", "banana", "cherry", "watermelon", "potato"]

print(fruits)
fruits.reverse()
print(fruits)
fruits.sort()
print(fruits)

fruits.insert(1, "tomato")
print(fruits)

ind = fruits.index('watermelon')
fruits.insert(ind - 1, 'cucumber')
print(fruits)
