from collections import defaultdict

# input
N, M = map(int, input().split())
S = input()
C = list(map(int, input().split()))
C_char = defaultdict(list)
# solve
for i in range(N):
    C_char[C[i]].append(S[i])
# output
p = [0] * M
ans = ""
for i in range(N):
    x = C[i]
    l = len(C_char[x])
    ans += C_char[x][(p[x - 1] - 1 + l) % l]
    p[x - 1] += 1

print(ans)
