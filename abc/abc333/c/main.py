from sys import stdin
input = stdin.readline

n = int(input())

ansl = []
repl = [int('1' * i) for i in range(1, 13)]
for i in range(12):
    for j in range(12):
        for k in range(12):
            x = repl[i] + repl[j] + repl[k]
            if x not in ansl:
                ansl.append(x)

ansl.sort()
print(ansl[n-1])
