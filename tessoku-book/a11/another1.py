def binary_search(x, n, a):
    l = 1
    r = n
    while l <= r:
        m = (l + r) // 2
        if x < a[m]:
            r = m - 1
        elif x == a[m]:
            return m
        elif x > a[m]:
            l = m + 1

    return -1

n, x = map(int, input().split())
a = [-1] + [*map(int, input().split())]

ans = binary_search(x, n, a)
print(ans)
