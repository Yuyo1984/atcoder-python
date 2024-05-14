def sigma_problem(n, A):
    MOD = 10**8

    # 全ての要素の総和
    total_sum = (n - 1) * sum(A)

    # 答えを求めるための変数
    result = 0

    # 部分和を求めるための累積和
    cumulative_sum = 0

    # 全ての要素について計算
    for i in range(n):
        cumulative_sum += A[i]
        result += (total_sum - cumulative_sum) % MOD
        result %= MOD

    return result


# 入力の例
n = int(input())
A = [*map(int, input().split())]

# 結果の出力
print(sigma_problem(n, A))
