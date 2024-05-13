def cnt_rem(N, A):
    cnt = [0] * (M+1)
    p = 0

    for num in A:
        cnt[num] += 1

    for i in range(M):
        cnt[i+1] += cnt[i]

    for num in A:
        p += N - cnt[M-num-1]
        if 2 * num >= M:
            p -= 1
    return p

N = int(input())
A = list(map(int, input().split()))
M = 10 ** 8

ans = (N-1) * sum(A) - cnt_rem(N, A) // 2 * M
print(ans)
