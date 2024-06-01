import bisect


def search(seq, x):
    return bisect.bisect_left(seq, x)


x = int(input())
A = [*map(int, input().split())]
A.sort()

print(search(A, x))
