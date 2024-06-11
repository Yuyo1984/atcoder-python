# input
N = int(input())
S = input()
# solve
ans = ""
stack = []
if S[0] == ",":
    stack.append(".")
else:
    stack.append(S[0])

for i in range(1, N):
    stack.append(S[i])
    if stack[0] != '"' and stack[-1] == ",":
        stack[-1] = "."
    if stack[0] != '"' and stack[-1] == '"':
        x = "".join(stack[:-1])
        ans += x
        del stack[0:-1]
    elif stack[0] == '"' and stack[-1] == '"' and len(stack) != 1:
        x = "".join(stack)
        ans += x
        stack.clear()

if len(stack) > 0:
    x = "".join(stack)
    ans += x
# output
print(ans)
