from itertools import accumulate

N = int(input())
A = [*map(int, input().split())]
M = int(input())
B = [int(input()) for i in range(M)]

meter_list = [0] + list(accumulate(A))

ans = 0
for i in range(1, M):
    ans += abs(meter_list[B[i] - 1] - meter_list[B[i - 1] - 1])
print(ans)
