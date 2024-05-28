def rotate(S, k):
    U = []
    for s in S:
        o_s = ord(s) + k
        if o_s >= 123:
            o_s = ord("a") + (o_s - 123)
        c = chr(o_s)
        U.append(c)
    return "".join(U)


S = input()
T = input()

rotated = []
for i in range(27):
    rotated.append(rotate(S, i))

if T in rotated:
    print("Yes")
else:
    print("No")
