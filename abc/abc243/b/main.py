n = int(input())
a = [*map(int, input().split())]
b = [*map(int, input().split())]

hit = 0
blow = 0

for i in range(n):
    if a[i] == b[i]:
        hit += 1
    else:
        if a[i] in b:
            blow += 1

print(hit)
print(blow)


