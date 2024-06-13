from functools import lru_cache


@lru_cache(maxsize=1000)
def calc(i):
    if i == 0:
        return 2
    elif i == 1:
        return 1
    else:
        return calc(i - 1) + calc(i - 2)


N = int(input())

print(calc(N))
