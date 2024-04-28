A = []
while True:
    x = input()
    A.append(x)
    if x == 'GB':
        break

A.sort()

print(A[6])
