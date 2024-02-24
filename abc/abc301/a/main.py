from sys import stdin
input = stdin.readline

N = int(input())
S = list(input().rstrip())

cnt_T = 0
cnt_A = 0
for i in S:
    if i == 'T':
        cnt_T += 1
    else:
        cnt_A += 1

if cnt_T > cnt_A:
    print('T')
elif cnt_T < cnt_A:
    print('A')
else:
    x = S[-1]
    if x == 'T':
        print('A')
    else:
        print('T')

