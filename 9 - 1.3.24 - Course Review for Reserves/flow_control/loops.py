i = 1
while i < 6:
    print(i)
    i += 1

# LOOP over list
fruits = ['apple', 'banana', 'kiwi']  # Array, in Python it's called List
for f in fruits:
    print(f)

# LOOP over range
for r in range(6):
    if r % 2 == 0:
        print(r)

print('range')
for r in range(4,19,3):
    print(f"[{r}]")
    # if r == 13:
    #     break
    if r % 2 != 0:
        if r > 9:
            continue
        print(r)
