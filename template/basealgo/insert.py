def insertion(A, i):
    t = A[i]
    j = i - 1

    while True:
        if not (j >= 0 and A[j] > t):
            break
        A[j + 1] = A[j]
        j -= 1
    A[j + 1] = t


def main():
    A = [*map(int, input().split())]

    print(*A)

    v = int(input())
    A.append(v)
    insertion(A, len(A) - 1)
    print(*A)


if __name__ == "__main__":
    main()
