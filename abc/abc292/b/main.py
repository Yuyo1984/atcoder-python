from sys import stdin
input = stdin.readline

N, Q = map(int, input().split())
checker = [0] * (N+1)
out = [False] * (N+1)
for i in range(Q):
    event = list(input().rstrip().split())
    x = int(event[1])
    if event[0] == '1':
        checker[x] += 1
        if checker[x] >= 2:
            out[x] = True
    elif event[0] == '2':
        out[x] = True
    else:
        if out[x]:
            print("Yes")
        else:
            print("No")

