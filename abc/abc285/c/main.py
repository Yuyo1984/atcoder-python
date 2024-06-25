S = input()[::-1]
l = len(S)
ans = 0
for i, x in enumerate(S):
    ans += (ord(x) - ord("A") + 1) * (26**i)
print(ans)
