N, Q = map(int, input().split())
S = input()
range_sum = [0 for i in range(N)]
for i in range(N):
    if S[i - 1] == S[i]:
        range_sum[i] += range_sum[i - 1] + 1
    else:
        range_sum[i] = range_sum[i - 1]
# print(*range_sum)
for i in range(Q):
    l, r = map(lambda x: int(x) - 1, input().split())
    print(range_sum[r] - range_sum[l])
