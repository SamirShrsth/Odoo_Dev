# list comprehension
# list = [expression for value in iterable *if condition*]

# multiply each value of x in range 0-10 by 2 if x is even
doubles = [x*2 for x in range(0,11) if x%2==0]

matrix = [[x for x in range(0,11)] for x in range(2)]
print(doubles)
print(matrix)
