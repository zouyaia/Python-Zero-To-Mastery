from random import choice

lst = [i for i in range(10, 151) if i%35==0]
print(choice(lst))