S = input()

l = [S[i : i + 3] for i in range(len(S) - 2)]

ans = float("inf")
for x in l:
    x = int(x)
    a = abs(x - 753)
    if a < ans:
        ans = a
print(ans)
