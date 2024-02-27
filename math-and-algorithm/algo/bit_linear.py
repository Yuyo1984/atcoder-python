N, S = map(int, input().split())
A = [*map(int, input().split())]

for i in range(0, 1<<N):
    sum = 0
    for j in range(1, N+1):
        # (i & 1 << (j-1)) != 0 の時、iの2進法表記の下からj桁目が1
        # 1 << (j-1)は2のj-1乗の意味
        if (i & (1 << (j-1))) != 0:
            sum += A[j-1]
    if sum == S:
        print("Yes")
        exit()
print("No")
