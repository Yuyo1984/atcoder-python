N = list(input())

while N[-1] == "0" and len(N) != 1:
    N.pop()

if N == N[::-1]:
    print("Yes")
else:
    print("No")
