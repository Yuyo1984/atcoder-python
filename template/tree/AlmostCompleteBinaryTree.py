def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


class AlmostCompleteBinaryTree:
    N = int(input())  # numbers of node
    keys = [input() for i in range(2 * N + 1)]

    for i in range(N):
        print(keys[left(i)])
        print(keys[right(i)])
