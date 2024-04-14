from sys import stdin
input = stdin.readline

N, K = map(int, input().split())
S = input().rstrip()

counter = 0
T = []
for i in range(N):
    if S[i] == 'o' and counter < K:
        counter += 1
        T.append('o')
    else:
        T.append('x')

print(''.join(T))
