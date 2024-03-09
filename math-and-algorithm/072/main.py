def solve(t):
    cl = (A + t - 1) // t
    cr = B // t
    if (cr - cl) >= 1:
        return True
    return False

A, B = map(int, input().split())
ans = 0
for i in range(1, B + 1):
    if solve(i):
        ans = i
print(ans)

