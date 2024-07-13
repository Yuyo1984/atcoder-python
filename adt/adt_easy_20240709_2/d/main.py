# input
S = input()
# solve
r1 = S.index("R")
r2 = S.rindex("R")
k = S.index("K")
b1 = S.index("B")
b2 = S.rindex("B")
# output
if (r1 < k < r2) and (b1 % 2 != b2 % 2):
    print("Yes")
else:
    print("No")
