s = 'aabbbccde'
d = {i:s.count(i) for i in s}
f = sorted(d.items(), key=lambda x: x[1], reverse=True)
for i in f:
    print(i[0], i[1])