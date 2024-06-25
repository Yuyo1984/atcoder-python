# input
N = int(input())
A = [*map(int, input().split())]
# solve
odd_nl = []
even_nl = []
for i in range(N):
    if A[i] % 2 == 0:
        even_nl.append(A[i])
    else:
        odd_nl.append(A[i])

odd_nl.sort(reverse=True)
even_nl.sort(reverse=True)

# output
el = len(even_nl)
ol = len(odd_nl)
if ol <= 1 and el <= 1:
    print(-1)
elif el <= 1:
    print(odd_nl[0] + odd_nl[1])
elif ol <= 1:
    print(even_nl[0] + even_nl[1])
else:
    x = odd_nl[0] + odd_nl[1]
    y = even_nl[0] + even_nl[1]
    print(max(x, y))
