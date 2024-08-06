def isOK(idx, key, A):
    if A[idx] >= key:
        return True
    else:
        return False


def bisect_search(key, A):
    left = -1
    right = len(A)

    while abs(right - left) > 1:
        mid = (left + right) // 2

        if isOK(mid, key, A):
            right = mid
        else:
            left = mid

    return right


def main():
    A = [*map(int, input().split())]
    values = [*map(int, input().split())]
    for v in values:
        print(bisect_search(v, A))


if __name__ == "__main__":
    main()
