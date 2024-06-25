def count(n, k):
    return k * (k - 1) ** (n - 1)


n, k = map(int, input().split())
print(count(n, k))
