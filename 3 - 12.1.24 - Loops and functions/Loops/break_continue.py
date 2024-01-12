fruits = ["apple", "banana", "cherry"]

print('Break example...')
for f in fruits:
    if f == "banana":
        break
    print(f)

print('Continue example...')
for f in fruits:
    if f == "banana":
        continue
    print(f)
