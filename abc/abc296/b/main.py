from sys import stdin
input = stdin.readline

s = []
for i in range(8):
    s.append(list(input()))

string = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
number = [i for i in range(8, 0, -1)]

for i in range(8):
    for j in range(8):
        if s[i][j] == '*':
            print(string[j] + str(number[i]))
            exit()
