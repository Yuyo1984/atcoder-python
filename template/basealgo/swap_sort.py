def swap(x, y):
    temp = x
    x = y
    y = temp
    return x, y


def main():
    a, b, c = map(int, input().split())
    if a > b:
        a, b = swap(a, b)
    if b > c:
        b, c = swap(b, c)
    if a > b:
        a, b = swap(a, b)

    print(a, b, c)


if __name__ == "__main__":
    main()
