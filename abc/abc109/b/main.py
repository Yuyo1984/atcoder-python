N = int(input())
W = [input() for i in range(N)]

flag = True
if len(set(W)) != N:
    print("No")
    exit()
for i in range(N):
    is_used = [True for i in range(N)]
    idx = i
    now_word = W[idx]
    is_used[idx] = False
    while True:
        for j in range(N):
            if j != idx and now_word[-1] == W[j][0] and is_used[j]:
                now_word = W[j]
                is_used[j] = False
                idx = j
        if j == N - 1:
            break
    if is_used.count(True) == 0:
        print("Yes")
        exit()
print("No")
