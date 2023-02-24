m = int(input())
a = [i for i in map(int, input().split())]
n = int(input())
b = [i for i in map(int, input().split())]
symd = list(set(a)^set(b))
print(*sorted(symd), sep='\n')