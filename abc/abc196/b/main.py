x = list(input())
ans = []
for c in x:
    if c == ".":
        break
    ans.append(c)
print("".join(ans))
