# func

# input
n, x, y, z = map(int, input().split())
if y <= x:
    x,y =y,x
if x <= z <= y:
    print("Yes")
else:
    print("No")
# solve

# answer
