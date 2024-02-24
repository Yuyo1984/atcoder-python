from sys import stdin
input = stdin.readline

a, b = map(int, input().split())
points = [4, 2, 1]
ans = 0
for i in range(3):
    flag_a = False
    flag_b = False
    p = points[i]
    if a - p >= 0:
        flag_a = True
        a -= p
    if b - p >= 0:
        flag_b = True
        b -= p
    if flag_a or flag_b:
        ans += p

print(ans)

