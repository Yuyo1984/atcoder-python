from itertools import count
import time

start_time = time.perf_counter_ns()

def GCD(N, M):
    ans = 0
    for i in count(1):
        if i > min(N, M):
            break
        if (N % i == 0 and M % i == 0):
            ans = i
    return ans

N, M = map(int, input().split())
print(GCD(N, M))

end_time = time.perf_counter_ns()

execution_time = end_time - start_time
print(f"実行時間: {execution_time}ナノ秒")
