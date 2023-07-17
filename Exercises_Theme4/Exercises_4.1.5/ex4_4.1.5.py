# Implement a solution to sum all the elements in the list
from functools import reduce

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sumed_numbers = reduce(lambda x, y: x + y, num_list)
print(sumed_numbers)
