# Implement a solution to round the "numbers_list" values
# using the number of decimal places contained in "precision_list"

numbers_list = [9.56783, 7.57568, 3.00914, 6.2321]
precision_list = [2, 2, 3, 3]

formated_numbers = map((lambda x,y: round(x,y)), numbers_list, precision_list)
print(list(formated_numbers))
