T = int(input())
for i in range(T):
    N = int(input())
    A = [*map(int, input().split())]
    ans = 0
    for i in A:
        if i % 2 == 1:
            ans += 1
    print(ans)

