a, b, c = map(int, input().split())
flag = False
if a+b >= c:
    flag = True

if flag:
    print("Yes")
else:
    print("No")
