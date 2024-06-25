import string

lower = string.ascii_lowercase
S = input()

ans = 0

for i in range(1, len(S)):
    x = S[0:-i]
    h = len(x) // 2
    if x[:h] == x[h:]:
        if len(x) >= ans:
            ans = len(x)

print(ans)
