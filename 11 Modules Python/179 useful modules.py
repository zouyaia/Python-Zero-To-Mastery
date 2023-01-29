from collections import Counter, defaultdict, OrderedDict

li = [i//3 for i in range(1, 8)]
sent = 'blal bla bla python3'
print(Counter(li))
print(Counter(sent))

dt = defaultdict(lambda : "doesn't exist", {'a': 1, 'b': 2})
print(dt['c'])

d = OrderedDict({'a': 3, 'd': 2})
print(d)