from sys import stdin
input = stdin.readline

n = int(input())

checker = 0
ans = 0
div_list = []
for i in range(1, n+1):
    x = 0
    for j in range(1, n+1):
        if i % 2 == 0:
            break
        if i % j == 0:
            x += 1
        if i < j:
            break
    div_list.append(x)

for i in div_list:
    if i == 8:
        ans += 1

print(ans)


