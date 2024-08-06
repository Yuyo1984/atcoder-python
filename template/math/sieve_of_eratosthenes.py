def SieveOfEratosthenes(n):
    is_prime = [False, False] + [True] * (n - 1)
    for p in range(2, n + 1):
        if not (is_prime[p]):
            continue
        for k in range(p * 2, n + 1, p):
            is_prime[k] = False
    return is_prime


def main():
    is_prime = SieveOfEratosthenes(int(input()))
    ansl = list()
    for i, x in enumerate(is_prime):
        if x:
            ansl.append(i)

    print(*ansl)


if __name__ == "__main__":
    main()
