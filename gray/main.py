from random import randint

N = int(input())

a = [2 * i + 1 for i in range(N + 1)]
in_num = int(input())
while in_num != 0:
    x = randint(0, len(a))
    ans = a.pop(a[x])
    print(ans, flush=True)

    in_num = int(input())
