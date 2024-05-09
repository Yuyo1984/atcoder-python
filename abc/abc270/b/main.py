x, y, z = map(int, input().split())

ans = 0

if x < 0:
    x = -x
    y = -y
    z = -z

if y < x and y > 0:
    if z < y and z > 0:
        ans += x
    elif z < y and z < 0:
        ans += (-z) * 2 + x
    else:
        ans = -1
elif y < 0 or y > x:
    ans += x

print(ans)
