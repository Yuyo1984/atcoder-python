n = int(input())
a = [*map(int, input().split())]
ans = 0
safe_flower = [9, 7, 3, 1]
for x in a:
    sub = 0
    for y in safe_flower:
        if x >= y:
            sub = x - y
            ans += sub
            break

print(ans)
