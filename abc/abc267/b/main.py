S = input()

is_existed = [True for i in range(10)]
for i in range(len(S)):
    if S[i] == "0":
        is_existed[i] = False

line = [1, 1, 1, 1, 1, 1, 1]
if not (is_existed[6]):
    line[0] = 0
if not (is_existed[3]):
    line[1] = 0
if not (is_existed[1]) and not (is_existed[7]):
    line[2] = 0
if not (is_existed[0]) and not (is_existed[4]):
    line[3] = 0
if not (is_existed[2]) and not (is_existed[8]):
    line[4] = 0
if not (is_existed[5]):
    line[5] = 0
if not (is_existed[9]):
    line[6] = 0
flag = False
if not (is_existed[0]):
    for i in range(5):
        if line[i] == 1 and line[i + 1] == 0 and line[i + 2 :].count(1) >= 1:
            flag = True

if flag:
    print("Yes")
else:
    print("No")
