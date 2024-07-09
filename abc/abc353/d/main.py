from itertools import accumulate

# input
N = int(input())
A = [*map(int, input().split())]
l = [len(str(x)) for x in A]
# solve
ans = 0
for i in range(N):
    s = A[i]
    ans += s
    ans %= 998244353
# output
print(ans)
