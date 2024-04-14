from sys import stdin
input = stdin.readline

N, A, B = map(int, input().split())

rem = N % (A + B)
ans = N // (A + B) * A
ans += min(rem, A)

print(ans)

