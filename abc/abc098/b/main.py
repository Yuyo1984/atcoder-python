N = int(input())
S = input()
ans = 0
for i in range(1, len(S) - 1):
    x = set(list(S[0:i]))
    y = set(list(S[i:]))
    if len(x & y) >= ans:
        ans = len(x & y)
print(ans)
