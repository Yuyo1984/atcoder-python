from functools import cache


@cache
def calc(N):
    if N == 1:
        return 0
    else:
        return calc(N // 2) + calc((N + 1) // 2) + N


# input
N = int(input())
# solve
ans = calc(N)
# output
print(ans)
