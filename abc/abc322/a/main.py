from sys import stdin
input = stdin.readline

N = int(input())
S = input().rstrip()
ans = S.find('ABC')
if ans == -1:
    print(ans)
else:
    print(ans+1)
