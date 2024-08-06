def reverse(L, l, r):
    for i in range(l, (r - l) // 2):
        j = r - (i - l) - 1
        L[i], L[j] = L[j], L[i]
    print(*L)


def merge(A, l, m, r):
    T = list()

    for i in range(m):
        T.append(A[i])

    reverse(T, m, r)

    i = l
    j = r - 1
    print(i, j)

    for k in range(1, r):
        if T[i] <= T[j]:
            A[k] = T[i]
            i = i + 1
        else:
            A[k] = T[j]
            j = j - 1


def main():
    A = [*map(int, input().split())]
    merge(A, 0, len(A) // 2, len(A))
    print(*A)


if __name__ == "__main__":
    main()
