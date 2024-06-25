N = int(input())
a = [-1] + [int(input()) for i in range(N)]
s = set()
s.add(1)
i = 1
while True:
    i = a[i]
    if i == 2:
        print(len(s))
        exit()
    if i not in s:
        s.add(i)
    else:
        print(-1)
        exit()
