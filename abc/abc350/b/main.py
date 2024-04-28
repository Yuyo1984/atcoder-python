# func

# input
N, Q = map(int, input().split())
T = [*map(int, input().split())]
existed = [True] * (N+1)
ans = N
# solve
for i in range(Q):
    if existed[T[i]]:
        ans -= 1
    else:
        ans += 1
    existed[T[i]] = not existed[T[i]]
# answer
print(ans)
