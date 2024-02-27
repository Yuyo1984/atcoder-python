N, K = map(int, input().split())
A = [*map(int, input().split())]

if sum(A) % 2 != K % 2:
    print("No")
else:
    if sum(A) > K:
        print("No")
    else:
        print("Yes")

