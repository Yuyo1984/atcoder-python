def min_index(A, b, e):
    mi = b
    for i in range(b, e):
        if A[i] < A[mi]:
            mi = i
    return mi


def main():
    A = [*map(int, input().split())]
    a, b = map(int, input().split())
    print(min_index(A, a, b))


if __name__ == "__main__":
    main()
