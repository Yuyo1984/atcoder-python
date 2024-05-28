q = int(input())
stack = []

for i in range(q):
    q = list(input().split())
    if q[0] == '1':
        stack.append(q[1])
    elif q[0] == '2':
        print(stack[-1])
    elif q[0] == '3':
        stack.pop()
