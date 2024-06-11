a = int(input())
b = int(input())
ans = 0
if abs(a - b) > 5:
    ans = 10 - abs(a - b)
else:
    ans = abs(a - b)
print(ans)
