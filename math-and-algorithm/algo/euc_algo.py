import time

start_time = time.perf_counter_ns()

def GCD(N, M):
    while N >= 1 and M >= 1:
        if N < M:
            M = M % N
        else:
            N = N % M
    if M >= 1:
        return M
    return N

N, M = map(int, input().split())
print(GCD(N, M))
end_time = time.perf_counter_ns()
execution_time = end_time - start_time
print(f"実行時間: {execution_time}ナノ秒")
