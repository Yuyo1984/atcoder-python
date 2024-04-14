import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = [*map(int, input().split())]
A = [i for i in A if i <= K]
A = set(A)

ans = (K * (K + 1) // 2) - sum(A)

print(ans)
