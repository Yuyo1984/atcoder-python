N = int(input())
T = [*map(int, input().split())]
M = int(input())
total_time = sum(T)
for i in range(M):
    p, x = map(int, input().split())
    ans = total_time - T[p - 1] + x
    print(ans)
