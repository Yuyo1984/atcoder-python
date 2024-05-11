#input
n = int(input())
h = list(map(int, input().split()))
#solve
x = h[0]
for i in range(1, n):
    if h[i] > x:
        print(i+1)
        exit()

print(-1)
#output
