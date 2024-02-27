def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

n, r = map(int, input().split())
print(factorial(n) // (factorial(n-r) * factorial(r)))
