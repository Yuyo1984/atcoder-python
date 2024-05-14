a = int(input())

ans = 0

for i in range(1, a):
    j = a - i
    x = i * j
    if x > ans:
        ans = x

print(ans)

