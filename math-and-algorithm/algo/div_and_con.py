def solve(l, r):
    if r - l == 1:
        return A[l-1]
    m = (l + r) // 2
    s1 = solve(l, m)
    s2 = solve(m, r)
    return s1 + s2

N = int(input())
A = [*map(int, input().split())]

ans = solve(1, N+1)
print(ans)

