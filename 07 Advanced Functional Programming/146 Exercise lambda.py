my_list = [5, 4, 3]
# Square with lambda
print(list(map(lambda item: item**2, my_list)))

# List sorting second value of the tuple
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
print(sorted(a, key=lambda tup: tup[1]))
# Tricky question, but I got it in the end