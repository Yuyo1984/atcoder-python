from collections import defaultdict

# input
S = input()
# solve
cnt = 0
mp = defaultdict(int)
mp[0] = 1

for s in S:
    cnt ^= 1 << int(s)
    mp[cnt] += 1
ans = 0
for v in mp.values():
    ans += v * (v - 1) // 2

# output
print(ans)
