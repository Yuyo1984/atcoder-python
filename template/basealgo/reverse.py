def swap(x, y):
    temp = x
    x = y
    y = temp
    return x, y


def reverse(A, l, r):
    for i in range(l, l + (r - l) // 2):
        j = r - (i - l) - 1
        A[i], A[j] = swap(A[i], A[j])
    return A


def main():
    A = [*map(int, input().split())]
    l, r = map(int, input().split())
    A = reverse(A, l, r)
    print(*A)


if __name__ == "__main__":
    main()
