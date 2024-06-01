def prime_check(x):
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


Q = int(input())
for i in range(Q):
    x = int(input())
    if prime_check(x):
        print("Yes")
    else:
        print("No")
