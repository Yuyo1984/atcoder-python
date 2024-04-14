A, B = map(int, input().split())

ans = 0
x = 1
while x < B:
    x += A - 1
    ans += 1

print(ans)
