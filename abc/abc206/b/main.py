from sys import stdin
input = stdin.readline

def f(i):
    return (i * (i + 1)) // 2

n = int(input())

ng = 0
ok = 100000000
while (ok - ng) > 1:
    mid = (ok + ng) // 2
    if f(mid) < n:
        ng = mid
    else:
        ok = mid

print(ok)
