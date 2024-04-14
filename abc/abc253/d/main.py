from sys import stdin
input = stdin.readline
import math

N, A, B = map(int, input().split())

x = N // A
y = N // B
L = math.lcm(A, B)
z = N // L
sum_A = A * (x * (x + 1) // 2)
sum_B = B * (y * (y + 1) // 2)
sum_both = L * (z * (z + 1) // 2)
sum_N = N * (N + 1) // 2

ans = sum_N - sum_A - sum_B + sum_both
print(ans)

