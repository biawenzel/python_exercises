# Implement a solution that print the even numbers

numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

new_list = filter(lambda number: number % 2 == 0, numbers)
print(list(new_list))
