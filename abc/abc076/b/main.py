n = int(input())
k = int(input())

ans = float("inf")

for i in range(0, 1 << n):
    num = 1
    b = format(i, "b")
    if len(b) < n:
        b = "0" * (n - len(b)) + b
    for x in b:
        if x == "0":
            num *= 2
        elif x == "1":
            num += k
    if num < ans:
        ans = num
print(ans)
