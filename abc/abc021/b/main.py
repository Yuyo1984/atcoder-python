N = int(input())
a, b = map(int, input().split())
K = int(input())
P = [*map(int, input().split())]

flag = True
if a in P or b in P:
    flag = False
else:
    for x in P:
        if P.count(x) >= 2:
            flag = False

print("YES" if flag else "NO")
