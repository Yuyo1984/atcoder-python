x = [int(input()) for _ in range(4)]
a,b,c,d = x

print(min(a+c, a+d, b+c, b+d))

