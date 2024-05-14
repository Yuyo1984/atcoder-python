x, y = map(int, input().split())
g1 = (1, 3, 5, 7, 8, 10, 12)
g2 = (4, 6, 9, 11)

flag = False
if x in g1 and y in g1:
    flag = True
if x in g2 and y in g2:
    flag = True

if flag:
    print("Yes")
else:
    print("No")

