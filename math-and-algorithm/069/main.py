a, b, c, d = map(int, input().split())
ans = -2<<60
for i in [a, b]:
    for j in [c, d]:
        if i * j >= ans:
            ans = i * j

print(ans)

