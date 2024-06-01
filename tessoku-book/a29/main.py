def power(a, b, mod):
    result = 1
    a = a % mod
    while b > 0:
        if (b % 2) == 1:
            result = (result * a) % mod
        a = (a * a) % mod
        b = b // 2
        print(result, a, b)
    return result


a, b = map(int, input().split())
mod = 10**9 + 7
ans = power(a, b, mod)

print(ans)
