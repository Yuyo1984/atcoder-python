N = int(input())
S = input()

stack = []
stack.append("")
for c in S:
    if c == '(':
        stack.append("(")
    elif c == ')':
        if len(stack) == 1:
            stack[-1] += c
        else:
            stack.pop()
    else:
        stack[-1] += c

ans = ""
for t in stack:
    ans += t
print(ans)

