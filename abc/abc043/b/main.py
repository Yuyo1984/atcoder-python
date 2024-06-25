s = input()
ans = []
for x in s:
    if x == "0":
        ans.append(x)
    elif x == "1":
        ans.append(x)
    else:
        if len(ans) > 0:
            ans.pop()

print("".join(ans))
