from sys import stdin
input = stdin.readline

x = int(input())

ans = 1
bank = 101

while bank < x:
    bank = bank + bank // 100
    ans += 1

print(ans)
