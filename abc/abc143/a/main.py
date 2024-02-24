A, B = map(int, input().split())

if A - B * 2 <= 0:
    ans = 0
else:
    ans = A - B * 2

print(ans)
