n = int(input())

def factorial(x):
    ans = 1
    for i in range(1, x+1):
        ans *= i
    return ans

print(factorial(n))

