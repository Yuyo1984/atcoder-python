s = input()
t = input()

flag = True
x = len(s)
y = len(t)
if x > y:
    flag = False
for i in range(min(x, y)):
    if s[i] != t[i]:
        flag = False

if flag:
    print("Yes")
else:
    print("No")
