import collections

N = int(input())
S = input()

x = collections.deque()
x.append("b")
i = 0
if "".join(x) == S:
    print(i)
    exit()
while len(x) < N:
    i += 1
    if i % 3 == 1:
        x.appendleft("a")
        x.append("c")
    if i % 3 == 2:
        x.appendleft("c")
        x.append("a")
    if i % 3 == 0:
        x.appendleft("b")
        x.append("b")
    acs = "".join(x)
    if acs == S:
        print(i)
        exit()
print(-1)
