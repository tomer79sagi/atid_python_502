# 1 - import entire module
# import my_module
# my_module.greet('Tomer Sagi')

# 2 - import specific function
from my_module import greet, Car
greet('Tomer Sagi')
my_car = Car('Subaru', 'Legacy', 2016)

# 3 - import module and rename
# import my_module as utility
# utility.greet('Tomer Sagi')
# my_car = utility.Car('Subaru', 'Legacy', 2016)