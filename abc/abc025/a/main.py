s = input()
n = int(input())

x = 0
for i in range(5):
    for j in range(5):
        x += 1
        if x == n:
            print(s[i] + s[j])
            exit()

