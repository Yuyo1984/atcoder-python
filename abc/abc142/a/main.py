N = int(input())

a = N // 2
if N % 2 == 1:
    a += 1

print('{:.10f}'.format(a / N))
