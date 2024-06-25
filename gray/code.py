N = int(input())
S = input()

ans = ""
stack = []
for i in range(N):
    stack.append(S[i])
    if stack[0] != '"' and stack[-1] == ",":
        stack.pop()
        stack.append(".")
    if len(stack) != 1 and stack[0] == '"' and stack[-1] == '"':
        ans += "".join(stack)
        stack.clear()
ans += "".join(stack)
print(ans)
