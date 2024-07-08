# input
group = ["AB", "BC", "CD", "DE", "AE"]
# solve
s = "".join(sorted(list(input())))
t = "".join(sorted(list(input())))

# output
flag = False
if s in group and t in group:
    flag = True
elif s not in group and t not in group:
    flag = True

print("Yes" if flag else "No")
