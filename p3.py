# Write a python program to create a list of tuples from given list having number and its cube in each tuple.
c = [2, 3, 4, 5, 6]
tuple = [(num, num**3) for num in c]
print("List of Tuples:", tuple)