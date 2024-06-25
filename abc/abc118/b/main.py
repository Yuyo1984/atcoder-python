n, m = map(int, input().split())
ans = set([i + 1 for i in range(m)])

for i in range(n):
    k, *a = map(int, input().split())
    A = list(a)
    s = set(A)
    ans &= s

print(len(ans))
