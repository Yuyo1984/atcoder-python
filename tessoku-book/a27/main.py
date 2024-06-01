def calc(a, b):
    if a < b:
        a, b = b, a

    while True:
        r = a % b
        a = b
        if r == 0:
            return a
        b = r


A, B = map(int, input().split())
ans = calc(A, B)
print(ans)
