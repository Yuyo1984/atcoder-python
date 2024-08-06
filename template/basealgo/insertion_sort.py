def insertion(A, i):
    t = A[i]
    j = i - 1

    while True:
        if not (j >= 0 and A[j] > t):
            break
        A[j + 1] = A[j]
        j -= 1
    A[j + 1] = t


def InsertionSort(A, N):
    for i in range(1, N):
        insertion(A, i)


def main():
    A = [*map(int, input().split())]
    InsertionSort(A, len(A))
    print(*A)


if __name__ == "__main__":
    main()
