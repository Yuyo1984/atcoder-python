a, b, c = map(int, input().split())

flag = False
if (a + b == c) or (b + c == a) or (c + a == b):
    flag = True

if flag:
    print("Yes")
else:
    print("No")
