N, L = map(int, input().split())

tastes = [(L + i) for i in range(N)]

sum_all = sum(tastes)
ans = 0
checker = 10000000
for i in range(len(tastes)):
    sum_i = sum_all - tastes[i]
    pie_i = abs(sum_all - sum_i)
    if pie_i <= checker :
        ans = sum_i
    checker = pie_i

print(ans)

