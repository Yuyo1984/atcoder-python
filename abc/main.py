A = []
cnt = 0
while input()!="":
    A.append(int(input()))
    cnt += 1

for i in range(len(A)-1, -1, -1):
    print(A[i])

