import itertools
n, x = map(int, input().split())
L = [*map(int, input().split())]

points = [i for i in itertools.accumulate(L)]
print(len([i for i in points if i <= x])+1)
