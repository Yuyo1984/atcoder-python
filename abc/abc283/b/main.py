N = int(input())
A = [0] + [*map(int, input().split())]
Q = int(input())
for i in range(Q):
    q = list(input().split())
    if q[0] == '1':
        k = int(q[1])
        x = int(q[2])
        A[k] = x
    if q[0] == '2':
        k = int(q[1])
        print(A[k])
