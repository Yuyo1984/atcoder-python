n, m, c = map(int, input().split())
b = [*map(int, input().split())]
ans = 0
for i in range(n):
    a = [*map(int, input().split())]
    mul_sum = c
    for j, k in zip(a, b):
        mul_sum += j * k
    if mul_sum > 0:
        ans += 1

print(ans)
