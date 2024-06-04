N, M = map(int, input().split())
a = set(map(int, input().split()))

ansl = []
stack = []
for i in range(1, N + 1):
    stack.append(i)
    if i not in a:
        while stack:
            ansl.append(stack.pop())

print(*ansl)
