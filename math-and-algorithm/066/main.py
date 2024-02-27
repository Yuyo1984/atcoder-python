N, K = map(int, input().split())

cnt = 0
for a in range(1, N+1):
    for b in range(max(1, a-(K-1)), min(N, a+(K-1))+1):
        for c in range(max(1, a-(K-1)), min(N, a+(K-1))+1):
            if abs(b - c) <= K - 1:
                cnt += 1

print(N ** 3 - cnt)
