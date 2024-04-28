from string import ascii_lowercase
N = int(input())
S = input()

chars = ascii_lowercase
ans = [0] * 26

for c in chars:
    cnt = 0
    x = 0
    if c not in S:
        continue
    for i in range(N):
        if S[i] == c:
            x += 1
            if x > cnt:
                cnt = x
        else:
            x = 0
    ans[chars.index(c)] += cnt

print(sum(ans))

