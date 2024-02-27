def getDivisors(N):
    div = []
    for i in range(1, N):
        if i * i > N:
            break
        if N % i == 0:
            div.append(i)
            div.append(N // i)

    return div

N = int(input())
div = getDivisors(N)
div.sort()
for i in div:
    print(i)
