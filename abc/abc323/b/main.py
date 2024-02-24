from sys import stdin
input = stdin.readline

n = int(input())
list = []
for i in range(n):
    list.append(input().rstrip())

ans_dict = {}
for i in range(len(list)):
    ans_dict[i+1] = list[i].count('o')

ans_dict = sorted(ans_dict.items(),key=lambda x:x[1],reverse=True)

for i in range(len(ans_dict)):
    print(ans_dict[i][0], end=' ')

