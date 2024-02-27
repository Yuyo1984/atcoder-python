def factorization(N):
    div = []
    while N % 2 == 0:
        div.append(2)
        N //= 2
    i = 3
    while i * i <= N:
        if N % i == 0:
            div.append(i)
            N //= i
        else:
            i += 2
    if N != 1:
        div.append(N)
    return div

N = int(input())
div = factorization(N)
div.sort()
print(*div)
