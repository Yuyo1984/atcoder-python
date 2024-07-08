import math

# input
S = input()
# solve
cnt = [0] * 26

for x in S:
    cnt[ord(x) - ord("a")] += 1

ans = len(S) ** 2

# output
print(ans)
