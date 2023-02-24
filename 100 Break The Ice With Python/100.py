n = int(input())
a = {}
b = []
for i in range(n):
    s = input()
    if s not in a.keys():
        a[s] = 1
        b.append(s)
    else:
        a[s] += 1
print(len(b))
for i in b:
    print(a[i], end=' ')
