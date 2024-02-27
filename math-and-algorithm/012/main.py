def isprime(N):
    for i in range(2, N):
        if i * i > N:
            break
        else:
            if N % i == 0:
               return False

    return True


N = int(input())

if isprime(N):
    print("Yes")
else:
    print("No")
