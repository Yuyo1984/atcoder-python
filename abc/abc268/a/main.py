from sys import stdin
input = stdin.readline

set = set()
x = [*map(int, input().split())]
for i in x:
    set.add(i)
print(len(set))

