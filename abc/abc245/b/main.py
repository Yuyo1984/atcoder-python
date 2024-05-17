n = int(input())
a = [*map(int, input().split())]
c_l = [True] * 2001

for i in range(n):
    c_l[a[i]] = False

for i in range(2002):
    if c_l[i]:
        print(i)
        exit()
