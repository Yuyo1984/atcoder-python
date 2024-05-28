N = int(input())
terminal = [[-1 for _ in range(N)] for _ in range(N)]

containers = []
for i in range(N):
    containers.append(list(map(int, input().split())))

wrong_cnt = 0
falls_cnt = 0

S = ["" for _ in range(N)]
x = "PRRRRQLLLL" * 4 + "PRRRRQ"
for i in range(N):
    S[i] = x

for i in range(N):
    print(S[i])
