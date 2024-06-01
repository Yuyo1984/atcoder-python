def GCD(a, b):
    while a >= 1 and b >= 1:
        if a >= b:
            a = a % b
        else:
            b = b % a

    if a != 0:
        return a
    return b


a, b = map(int, input().split())
print(GCD(a, b))
