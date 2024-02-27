N = int(input())
B = [*map(int, input().split())]
R = [*map(int, input().split())]

print(sum(B) / N + sum(R) / N)
