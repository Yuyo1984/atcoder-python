n, k = map(int, input().split())
a = [-1] + [*map(int, input().split())]


def check(x):
    sum = 0
    for i in range(1, n + 1):
        sum += x // a[i]
    if sum >= k:
        return True
    return False


def binary_search():
    l = 1
    r = 10**9
    while l < r:
        m = (l + r) // 2
        ans = check(m)
        if not ans:
            l = m + 1
        if ans:
            r = m
    return l


ans = binary_search()
print(ans)
