N = int(input())
X = [*map(int, input().split())]
X.sort()

ans = sum(X[N:len(X)-N]) / (len(X)-N*2)
print(ans)
