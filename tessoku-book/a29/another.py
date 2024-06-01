def power(a, b, m):
    p = a
    ans = 1
    for i in range(30):
        div = 1 << i
        if (b // div) % 2 == 1:
            ans = (ans * p) % m
        p = (p * p) % m
        print(div, ans, p)
    return ans


a, b = map(int, input().split())
m = 10**9 + 7
print(power(a, b, m))
