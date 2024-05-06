n = int(input())
s = input()

for i in range(1, n):
    result = 0
    for j in range(n - i):
        if s[j] != s[i+j]:
            result += 1
        else:
            break
    print(result)

