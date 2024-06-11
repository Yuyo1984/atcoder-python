N = int(input())
A = [*map(int, input().split())]

x, y = 0, 0
for i in A:
    if i > 0:
        y += 1
    x += i
bug_cnt = (x + y - 1) // y
print(bug_cnt)
