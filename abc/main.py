N = int(input())
ans = ""

while len(ans) < 10:
    if N % 2 == 0:
        ans += "0"
    else:
        ans += "1"
    N //= 2

print(ans[::-1])
