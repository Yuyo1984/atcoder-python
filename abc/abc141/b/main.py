S = input()

flag1 = True
flag2 = True
for i in range(0, len(S)):
    if i % 2 == 1:
        if S[i] == 'R':
            flag1 = False
    else:
        if S[i] == 'L':
            flag2 = False
    if flag1 == False and flag2 == False:
        break

if flag1 and flag2:
    print("Yes")
else:
    print("No")

