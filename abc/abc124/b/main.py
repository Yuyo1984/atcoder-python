n = int(input())
h = [*map(int, input().split())]

ans = 0

for i in range(n):
    flag = True
    for j in range(0, i + 1):
        if h[i] < h[j]:
            flag = False
    if flag:
        ans += 1

print(ans)
