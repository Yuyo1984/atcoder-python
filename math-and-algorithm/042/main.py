def calc(n):
    divisor_cnt = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            divisor_cnt[j] += 1

    total_sum = 0
    for i in range(1, n + 1):
        total_sum += divisor_cnt[i] * i
    return total_sum


N = int(input())
print(calc(N))
