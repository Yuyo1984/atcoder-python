def swap(arr, i, j):
    res = arr[:]

    res[i], res[j] = res[j], res[i]

    return res


def partition(A, l, r):
    p = l
    i = p - 1
    for j in range(p, r):
        if A[j] < A[r]:
            i += 1
            A = swap(A, i, j)

    i += 1
    A = swap(A, i, r)
    return A, i


def main():
    A = [*map(int, input().split())]
    q, sv = partition(A, 0, len(A) - 1)
    print(q[sv])
    print(*q)


if __name__ == "__main__":
    main()
