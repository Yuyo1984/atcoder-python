N = int(input())
A = [*map(int, input().split())]
ans = 0
cnt = [0] * 100001
for i in range(N):
    cnt[A[i]] += 1

for i in range(1, 50001):
    if i == 50000:
        ans += (cnt[i] * (cnt[i]-1)) // 2
    else:
        ans += cnt[i] * cnt[100000-i]

print(ans)

