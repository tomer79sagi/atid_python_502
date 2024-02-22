# my_set = set({"Hamza", "Mahadi", "Baker"})
my_set = {"Hamza", "Mahadi", "Baker"}

print(my_set)
my_set.add("Elias")
print(my_set)
my_set.remove("Hamza")
print(my_set)
# my_set.remove("John")
my_set.discard("Mahadi")
print(my_set)
print(len(my_set))

print("Baker" in my_set)  # True
print("Michael" in my_set)  # False
