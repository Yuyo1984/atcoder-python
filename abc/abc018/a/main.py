a, b, c = [int(input()) for i in range(3)]
if a < b < c:
    ans = [3, 2, 1]
elif a < c < b:
    ans = [3, 1, 2]
elif b < a < c:
    ans = [2, 3, 1]
elif b < c < a:
    ans = [1, 3, 2]
elif c < a < b:
    ans = [2, 1, 3]
else:
    ans = [1, 2, 3]

for x in ans:
    print(x)
