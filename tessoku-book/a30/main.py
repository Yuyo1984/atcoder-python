def power(a, b, m):
    p = a
    ans = 1
    for i in range(30):
        div = 1 << i
        if (b // div) % 2 == 1:
            ans = (ans * p) % m
        p = (p * p) % m
    return ans


def division(a, b, m):
    return (a * power(b, m - 2, m)) % m


m = 10**9 + 7
n, r = map(int, input().split())

a = 1
for i in range(1, n + 1):
    a = (a * i) % m

b = 1
for i in range(1, r + 1):
    b = (b * i) % m
for i in range(1, n - r + 1):
    b = (b * i) % m

print(division(a, b, m))
