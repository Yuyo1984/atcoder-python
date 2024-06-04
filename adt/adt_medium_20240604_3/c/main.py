# input
S = input()
# solve
b_l = -1
b_r = -1
r_l = -1
r_r = -1
k_idx = -1
for x in range(8):
    if S[x] == "B" and b_l == -1:
        b_l = x
    if S[x] == "B" and b_l != -1:
        b_r = x
    if S[x] == "R" and r_l == -1:
        r_l = x
    if S[x] == "R" and r_l != -1:
        r_r = x
    if S[x] == "K":
        k_idx = x


# output
if b_l % 2 != b_r % 2 and r_l < k_idx < r_r:
    print("Yes")
else:
    print("No")
