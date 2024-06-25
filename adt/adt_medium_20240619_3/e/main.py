# input
n, m = map(int, input().split())
s = list(input().split())
t = set(list(input().split()))
# solve
for x in s:
    if x in t:
        print("Yes")
    else:
        print("No")
# output
