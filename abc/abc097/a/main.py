a, b, c, d = map(int, input().split())

flag = False
if abs(c-a) <= d:
    flag = True
elif abs(b-a) <= d and abs(c-b) <= d:
    flag = True

if flag:
    print("Yes")
else:
    print("No")

