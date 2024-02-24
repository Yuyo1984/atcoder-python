from sys import stdin
input = stdin.readline

def f(t):
    cnt = 0
    for w, x in wx:
        time = (x + t) % 24
        if 9 <= time <= 17:
            cnt += w
    return cnt

n = int(input())
wx = [[*map(int, input().split())] for _ in range(n)]
print(f(t) for t in range(24))
ans = max(f(t) for t in range(24))
print(ans)
