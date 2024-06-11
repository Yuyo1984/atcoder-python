# input
S = input()
# solve
c_l = 0
c_u = 0

for c in S:
    if c.islower():
        c_l += 1
    else:
        c_u += 1
# output
if c_u > c_l:
    S = S.upper()
else:
    S = S.lower()
print(S)
