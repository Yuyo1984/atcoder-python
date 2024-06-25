# input
n, k = map(int, input().split())
S = [input() for i in range(n)]
# solve
x = sorted(S[0:k])
for name in x:
    print(name)

# output
